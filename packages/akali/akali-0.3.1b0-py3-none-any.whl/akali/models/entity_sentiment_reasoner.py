from pydantic import BaseModel
from typing import List


class EntitySentimentReasonerResult(BaseModel):
    entity: str
    sentiment: str
    reason: str


class EntitySentimentReasonerOutput(BaseModel):
    entity_list: List[str]
    results: List[EntitySentimentReasonerResult]