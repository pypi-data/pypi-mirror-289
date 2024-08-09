from .entity_sentiment_reasoner import EntitySentimentReasonerComparisonCriteria
from .text_classification import TextClassificationComparisonCriteria
from .comparison_criteria import ComparisonCriteria


class ComparisonCriteriaFactory:
    @staticmethod
    def get_criteria(task_name: str) -> ComparisonCriteria:
        criteria_map = {
            "EntitySentimentReasoner": EntitySentimentReasonerComparisonCriteria(),
            "TextClassification": TextClassificationComparisonCriteria(),
            # Add more mappings as you define more criteria
        }
        return criteria_map.get(task_name, ComparisonCriteria())