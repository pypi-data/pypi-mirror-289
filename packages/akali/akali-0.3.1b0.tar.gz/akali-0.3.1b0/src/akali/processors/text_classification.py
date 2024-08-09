from typing import Dict, Any
from ..models.text_classification import TextClassificationResult, TextClassificationOutput


def text_classification_processor(result: str) -> Dict[str, Any]:
    lines = result.strip().split('\n')
    results = []
    for line in lines:
        parts = line.split('|')
        if len(parts) == 2:
            label = parts[0].strip()
            confidence = float(parts[1].strip())
            results.append(TextClassificationResult(
                label=label,
                confidence=confidence
            ))
    return TextClassificationOutput(results=results).dict()