# src/akali/processors/entity_sentiment_processor.py
from typing import Dict, Any
from ..models.entity_sentiment import EntitySentimentResult, EntitySentimentOutput


def entity_sentiment_processor_without_reason(result: str) -> Dict[str, Any]:
    lines = result.strip().split('\n')
    entity_list = []
    results = []
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 2:
            entity = parts[0].strip()

            sentiment = parts[1].strip()
            if sentiment.lower() == "negative" or sentiment.lower() == "negatif" or sentiment.lower() == "olumsuz":
                sentiment = "olumsuz"
            elif sentiment.lower() == "positive" or sentiment.lower() == "pozitif" or sentiment.lower() == "olumlu":
                sentiment = "olumlu"
            else:
                sentiment = "nötr"

            if entity not in entity_list:
                entity_list.append(entity)

            entity_result = EntitySentimentResult(
                entity=entity,
                sentiment=sentiment,
            )
            if entity_result not in results:
                results.append(entity_result)

    return EntitySentimentOutput(entity_list=entity_list, results=results).dict()
