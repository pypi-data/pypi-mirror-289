# evaluators.py

from korouge_score import rouge_scorer
from typing import Union, List
import math

# OfflineRetrievalEvaluators 클래스 정의
class OfflineRetrievalEvaluators:
    # 초기화 메서드: 실제 문서, 예측 문서, 매칭 방법, 임계값을 인자로 받음
    def __init__(self, actual_docs, predicted_docs, match_method="text", threshold=0.8):
        self.actual_docs = actual_docs  # 실제 문서 리스트
        self.predicted_docs = predicted_docs  # 예측 문서 리스트
        self.match_method = match_method  # 매칭 방법 ('text', 'rouge1', 'rouge2', 'rougeL' 중 하나)
        self.threshold = threshold  # ROUGE 점수를 사용할 경우의 임계값
        self.scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)  # ROUGE 점수 계산기

    # 실제 텍스트와 예측 텍스트를 비교하는 메서드
    def text_match(self, actual_text: str, predicted_text: Union[str, List[str]]) -> bool:
        """
        실제 텍스트와 예측 텍스트가 일치하는지 확인하는 함수.
        """
        
        # 단순 텍스트 매칭 방법을 사용할 경우
        if self.match_method == "text":
            if isinstance(predicted_text, str):
                return actual_text in predicted_text
            # 예측 텍스트가 리스트인 경우, 리스트 내 텍스트 중 하나라도 일치하면 True 반환
            elif isinstance(predicted_text, list):
                return any(actual_text in text for text in predicted_text)
            else:
                raise ValueError("predicted_text must be a string or a list of strings.")        
        
        # ROUGE 점수를 이용한 매칭 방법
        elif self.match_method in ["rouge1", "rouge2", "rougeL"]:
            scores = self.scorer.score(actual_text, predicted_text)
            score = scores[self.match_method].fmeasure  # fmeasure 값을 사용하여 매칭
            return score >= self.threshold  # ROUGE 점수가 임계값 이상이면 True 반환
        else:
            raise ValueError("Invalid match method specified.")  # 잘못된 매칭 방법이 지정된 경우 예외 발생

    # Hit Rate 계산: 실제 문서와 예측 문서가 일치하는 비율 계산
    def calculate_hit_rate(self) -> float:
        total_hits = 0  # 전체 일치 횟수
        total_docs = 0  # 전체 실제 문서 수
        
        # 실제 문서 리스트와 예측 문서 리스트를 반복
        for actual_docs, predicted_docs in zip(self.actual_docs, self.predicted_docs):
            match_count = 0  # 현재 문서 쌍에 대한 일치 횟수
            for actual_doc in actual_docs:
                actual_text = actual_doc.page_content
                # 예측 문서들 중 하나라도 실제 문서와 일치하는 경우
                if self.text_match(actual_text, [pred_doc.page_content for pred_doc in predicted_docs]):
                    match_count += 1  # 일치 횟수 증가
            
            total_hits += match_count  # 전체 일치 횟수 업데이트
            total_docs += len(actual_docs)  # 전체 실제 문서 수 업데이트
        
        # 전체 일치 횟수를 전체 문서 수로 나눠서 Hit Rate 반환
        return total_hits / total_docs if total_docs > 0 else 0.0
    
    # MRR (Mean Reciprocal Rank) 계산: 첫 번째로 일치한 문서의 순위를 바탕으로 평균 역수를 계산
    def calculate_mrr(self) -> float:
        cumulative_reciprocal = 0  # 누적 역수 합
        Q = len(self.actual_docs)  # 전체 쿼리 수 (실제 문서 리스트의 길이)
        
        # 실제 문서 리스트와 예측 문서 리스트를 반복
        for actual_docs, predicted_docs in zip(self.actual_docs, self.predicted_docs):
            for rank, predicted_doc in enumerate(predicted_docs, start=1):
                # 예측 문서 중 첫 번째로 실제 문서와 일치하는 경우
                if any(self.text_match(actual_doc.page_content, predicted_doc.page_content) for actual_doc in actual_docs):
                    cumulative_reciprocal += 1 / rank  # 해당 순위의 역수를 누적
                    break  # 첫 번째 일치 문서를 찾으면 루프 종료
        
        # 누적 역수를 전체 쿼리 수로 나눠서 MRR 반환
        return cumulative_reciprocal / Q if Q > 0 else 0.0

    # Recall@k 계산: 상위 k개의 예측 문서 중 실제 문서가 포함된 비율 계산
    def calculate_recall_k(self, k: int) -> float:
        total_recall = 0  # 전체 Recall 합
        total_docs = 0  # 전체 실제 문서 수
        
        # 실제 문서 리스트와 예측 문서 리스트를 반복
        for actual_docs, predicted_docs in zip(self.actual_docs, self.predicted_docs):
            match_count = 0  # 현재 문서 쌍에 대한 일치 횟수
            top_k_predicted_texts = [pred_doc.page_content for pred_doc in predicted_docs[:k]]  # 상위 k개의 예측 텍스트
            
            for actual_doc in actual_docs:
                actual_text = actual_doc.page_content
                # 실제 문서가 상위 k개의 예측 문서에 포함된 경우
                if self.text_match(actual_text, top_k_predicted_texts):
                    match_count += 1  # 일치 횟수 증가
            
            total_recall += match_count  # 전체 Recall 합 업데이트
            total_docs += len(actual_docs)  # 전체 실제 문서 수 업데이트
        
        # 전체 Recall 합을 전체 문서 수로 나눠서 Recall@k 반환
        return total_recall / total_docs if total_docs > 0 else 0.0
    
    # Precision@k 계산: 상위 k개의 예측 문서 중 실제 문서가 포함된 비율 계산
    def calculate_precision_k(self, k: int) -> float:
        total_precision = 0  # 전체 Precision 합
        total_queries = len(self.actual_docs)  # 전체 쿼리 수
        
        # 실제 문서 리스트와 예측 문서 리스트를 반복
        for actual_docs, predicted_docs in zip(self.actual_docs, self.predicted_docs):
            match_count = 0  # 현재 문서 쌍에 대한 일치 횟수
            top_k_predicted_texts = [pred_doc.page_content for pred_doc in predicted_docs[:k]]  # 상위 k개의 예측 텍스트
            
            for predicted_text in top_k_predicted_texts:
                # 예측 문서가 실제 문서 중 하나와 일치하는 경우
                if any(self.text_match(actual_doc.page_content, predicted_text) for actual_doc in actual_docs):
                    match_count += 1  # 일치 횟수 증가
            
            total_precision += match_count / k  # 전체 Precision 합 업데이트
        
        # 전체 Precision 합을 전체 쿼리 수로 나눠서 Precision@k 반환
        return total_precision / total_queries if total_queries > 0 else 0.0

    # MAP@k (Mean Average Precision at k) 계산: 상위 k개의 예측 문서에 대해 평균 Precision을 계산
    def calculate_map_k(self, k: int) -> float:
        total_map = 0  # 전체 MAP 합
        total_queries = len(self.actual_docs)  # 전체 쿼리 수
        
        # 실제 문서 리스트와 예측 문서 리스트를 반복
        for actual_docs, predicted_docs in zip(self.actual_docs, self.predicted_docs):
            num_relevant = 0  # 관련 문서 수
            precision_at_i = 0  # i번째 문서까지의 Precision 합
            
            # 상위 k개의 예측 문서에 대해 반복
            for i, predicted_doc in enumerate(predicted_docs[:k], start=1):
                # 예측 문서가 실제 문서 중 하나와 일치하는 경우
                if any(self.text_match(actual_doc.page_content, predicted_doc.page_content) for actual_doc in actual_docs):
                    num_relevant += 1  # 관련 문서 수 증가
                    precision_at_i += num_relevant / i  # Precision 계산 후 누적
            
            total_map += precision_at_i / num_relevant if num_relevant > 0 else 0  # 관련 문서가 있을 경우 MAP 계산 후 누적
        
        # 전체 MAP 합을 전체 쿼리 수로 나눠서 MAP@k 반환
        return total_map / total_queries if total_queries > 0 else 0.0

    # DCG (Discounted Cumulative Gain) 계산: 주어진 순위에서의 관련성을 바탕으로 누적 이득 계산
    def dcg_at_k(self, relevance_scores: List[int], k: int) -> float:
        dcg = 0.0  # DCG 값 초기화
        for i in range(min(len(relevance_scores), k)):
            # 순위에 따라 로그 스케일로 감소된 이득을 누적
            dcg += relevance_scores[i] / math.log2(i + 2)
        return dcg  # 최종 DCG 값 반환

    def ndcg_at_k(self, k: int) -> float:
        total_ndcg = 0  # 전체 NDCG 합
        total_queries = len(self.actual_docs)  # 전체 쿼리 수
        
        # 실제 문서 리스트와 예측 문서 리스트를 반복
        for actual_docs, predicted_docs in zip(self.actual_docs, self.predicted_docs):
            relevance_scores = []
            
            # ROUGE 점수를 사용한 관련성 평가 또는 이진 관련성 평가
            if self.match_method in ["rouge1", "rouge2", "rougeL"]:
                for pred_doc in predicted_docs[:k]:
                    # 각 예측 문서에 대해 모든 실제 문서와 비교하여 가장 높은 ROUGE 점수 사용
                    max_score = max(
                        self.scorer.score(actual_doc.page_content, pred_doc.page_content)[self.match_method].fmeasure
                        for actual_doc in actual_docs
                    )
                    relevance_scores.append(max_score)

            else:
                # 이진 관련성 평가: 일치하는 경우 1, 그렇지 않으면 0
                relevance_scores = [1 if any(self.text_match(actual_doc.page_content, pred_doc.page_content) 
                                            for actual_doc in actual_docs) else 0 for pred_doc in predicted_docs[:k]]
            
            ideal_relevance_scores = sorted(relevance_scores, reverse=True)  # 이상적인 관련성 점수 리스트

            print(relevance_scores)
            print(ideal_relevance_scores)
            
            dcg = self.dcg_at_k(relevance_scores, k)  # DCG 계산
            idcg = self.dcg_at_k(ideal_relevance_scores, k)  # 이상적인 DCG 계산
            
            total_ndcg += dcg / idcg if idcg > 0 else 0.0  # NDCG 계산 후 누적
        
        # 전체 NDCG 합을 전체 쿼리 수로 나눠서 NDCG@k 반환
        return total_ndcg / total_queries if total_queries > 0 else 0.0

