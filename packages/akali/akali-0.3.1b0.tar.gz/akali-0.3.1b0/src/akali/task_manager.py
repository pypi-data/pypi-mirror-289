from typing import Callable, Type
from pydantic import BaseModel

from .models import *
from .processors import *


class Task:
    def __init__(self, name: str, processor: Callable, output_model: Type[BaseModel]):
        self.name = name
        self.processor = processor
        self.output_model = output_model


class TaskManager:
    @staticmethod
    def get_task(task: str) -> Task:
        tasks = {
            "EntitySentimentReasoner": Task(
                name=task,
                processor=entity_sentiment_processor,
                output_model=EntitySentimentReasonerOutput
            ),
            "EntitySentiment": Task(
                name=task,
                processor=entity_sentiment_processor_without_reason,
                output_model=EntitySentimentOutput
            ),
            "TextClassification": Task(
                name=task,
                processor=text_classification_processor,
                output_model=TextClassificationOutput
            )
        }
        if task not in tasks:
            raise ValueError(f"Unsupported task: {task}")
        return tasks[task]