from pydantic import BaseModel
from typing import List


class TextClassificationResult(BaseModel):
    label: str
    confidence: float


class TextClassificationOutput(BaseModel):
    results: List[TextClassificationResult]