# src/akali/processors/entity_sentiment_processor.py
from typing import Dict, Any
from ..models.entity_sentiment_reasoner import EntitySentimentReasonerResult, EntitySentimentReasonerOutput


def entity_sentiment_processor(result: str) -> Dict[str, Any]:
    lines = result.strip().split('\n')
    entity_list = []
    results = []
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 2:
            entity = parts[0].strip()
            sentiment = parts[1].strip()
            reason = parts[2].strip() if len(parts) > 2 else "unknown"
            entity_list.append(entity)
            results.append(EntitySentimentReasonerResult(
                entity=entity,
                sentiment=sentiment,
                reason=reason
            ))
    return EntitySentimentReasonerOutput(entity_list=entity_list, results=results).dict()
