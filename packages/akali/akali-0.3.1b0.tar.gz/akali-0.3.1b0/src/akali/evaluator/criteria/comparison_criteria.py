from abc import ABC, abstractmethod
from typing import Dict, Any


class ComparisonCriteria(ABC):
    @abstractmethod
    def compare(self, ground_truth: Dict[str, Any], prediction: Dict[str, Any]) -> Dict[str, Any]:
        pass
