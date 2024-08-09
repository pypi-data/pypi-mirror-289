from typing import Dict, Any
from .comparison_criteria import ComparisonCriteria


class EntitySentimentReasonerComparisonCriteria(ComparisonCriteria):
    def compare(self, ground_truth: Dict[str, Any], prediction: Dict[str, Any]) -> Dict[str, Any]:
        entity_correct = ground_truth['entity'] == prediction['entity']
        sentiment_correct = ground_truth['sentiment'] == prediction['sentiment']
        reason_similarity = self.calculate_similarity(ground_truth['reason'], prediction['reason'])

        return {
            'entity_accuracy': 1 if entity_correct else 0,
            'sentiment_accuracy': 1 if sentiment_correct else 0,
            'reason_similarity': reason_similarity,
            'overall_accuracy': (entity_correct + sentiment_correct + (reason_similarity > 0.8)) / 3
        }

    def calculate_similarity(self, text1: str, text2: str) -> float:
        # Placeholder value
        return 0.5