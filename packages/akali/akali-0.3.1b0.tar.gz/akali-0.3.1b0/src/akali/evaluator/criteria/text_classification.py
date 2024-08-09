from typing import Dict, Any
from .comparison_criteria import ComparisonCriteria


class TextClassificationComparisonCriteria(ComparisonCriteria):
    def compare(self, ground_truth: Dict[str, Any], prediction: Dict[str, Any]) -> Dict[str, Any]:
        label_correct = ground_truth['label'] == prediction['label']
        confidence = prediction.get('confidence', 1.0)

        return {
            'label_accuracy': 1 if label_correct else 0,
            'confidence': confidence,
            'overall_score': confidence if label_correct else 0
        }