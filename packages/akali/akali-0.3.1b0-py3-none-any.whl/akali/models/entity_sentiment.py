from pydantic import BaseModel
from typing import List


class EntitySentimentResult(BaseModel):
    entity: str
    sentiment: str


class EntitySentimentOutput(BaseModel):
    entity_list: List[str]
    results: List[EntitySentimentResult]