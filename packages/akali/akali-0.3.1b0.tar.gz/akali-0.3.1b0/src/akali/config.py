from typing import Dict, Any, Callable


class AugmenterConfig:
    def __init__(self,
                 metric_extractors: Dict[str, Callable[[Dict[str, Any]], float]],
                 strategy_conditions: Dict[str, Callable[[Dict[str, float]], float]],
                 score_adjustments: Callable[[Dict[str, float], Dict[str, float]], Dict[str, float]],
                 augmentation_strategies: Dict[str, Callable]):
        self.metric_extractors = metric_extractors
        self.strategy_conditions = strategy_conditions
        self.score_adjustments = score_adjustments
        self.augmentation_strategies = augmentation_strategies
