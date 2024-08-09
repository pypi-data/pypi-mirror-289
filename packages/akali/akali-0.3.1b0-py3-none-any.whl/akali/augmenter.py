import re
import random
from collections import defaultdict
from typing import List, Dict, Any

from .language_interface import LanguageInterface
from .task_manager import TaskManager
from .evaluator import ComparisonCriteriaFactory, ComparisonCriteria, Evaluator
from .config import AugmenterConfig


class AggressiveKnowledgeAugmenter:
    def __init__(
            self,
            mentee: LanguageInterface,
            mentor: LanguageInterface,
            task: str | ComparisonCriteria,
            analysis_config: AugmenterConfig,
    ):
        self.mentee = mentee
        self.mentor = mentor
        self.task = TaskManager.get_task(task)
        self.config = analysis_config
        self.comparison_criteria = ComparisonCriteriaFactory.get_criteria(task) \
            if isinstance(task, str) else task
        self.evaluator = Evaluator(self.comparison_criteria, analysis_config)
        self.augmentation_strategies = {
            "entity_swapping": self.entity_swapping,
            "sentence_restructuring": self.sentence_restructuring,
            "paraphrase_with_mentor": self.paraphrase_with_mentor,
            "generate_contrasting_examples": self.generate_contrasting_examples,
            "entity_attribute_expansion": self.entity_attribute_expansion,
            "contextual_example_generation": self.contextual_example_generation,
            "sentiment_intensity_variation": self.sentiment_intensity_variation,
            "cross_domain_adaptation": self.cross_domain_adaptation,
        }
        self.proposed_strategies = []
        self.test_results = []

    def compare_prediction(self, ground_truth: Dict[str, Any], prediction: Dict[str, Any]) -> Dict[str, Any]:
        return self.comparison_criteria.compare(ground_truth, prediction)

    def evaluate(self, test_data: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        results = []
        for item in test_data:
            self.task.output_model(**item)
            mentee_prediction = self.mentee.predict(**item)
            comparison_result = self.compare_prediction(item, mentee_prediction)
            results.append({
                "ground_truth": item,
                "prediction": mentee_prediction,
                "comparison_result": comparison_result
            })
        self.test_results = results
        return {"results": results}

    def propose(self) -> List[str]:
        strategy_scores = self.evaluator.analyze_results(self.test_results)
        selected_strategies = [strategy for strategy, score in strategy_scores.items() if score > 0.5]
        self.proposed_strategies = selected_strategies
        return self.proposed_strategies

    def augment(self, train_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = train_data.copy()

        for strategy_name in self.proposed_strategies:
            if strategy_name not in self.augmentation_strategies:
                print(f"Warning: Strategy '{strategy_name}' not found. Skipping.")
                continue

            strategy_func = self.augmentation_strategies[strategy_name]
            print(f"Info: Applying {strategy_name} strategy...")

            try:
                new_examples = strategy_func(train_data)
                augmented_data.extend(new_examples)
                print(f"Info: Generated {len(new_examples)} new examples using {strategy_name}")
            except Exception as e:
                print(f"Error: Error applying {strategy_name}: {str(e)}")

        print(f"Info: Augmentation complete. Total examples: {len(augmented_data)}")
        return augmented_data

    def entity_swapping(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        sentiment_entities = defaultdict(list)
        for item in data:
            sentiment_entities[item['sentiment']].append(item['entity'])

        augmented_data = []
        for item in data:
            new_item = item.copy()
            same_sentiment_entities = [e for e in sentiment_entities[item['sentiment']] if e != item['entity']]

            if same_sentiment_entities:
                new_entity = random.choice(same_sentiment_entities)
            else:
                all_other_entities = [e for e in sum(sentiment_entities.values(), []) if e != item['entity']]
                new_entity = random.choice(all_other_entities) if all_other_entities else item['entity']

            if new_entity != item['entity']:
                new_item['entity'] = new_entity
                new_item['reason'] = re.sub(r'\b' + re.escape(item['entity']) + r'\b', new_entity, new_item['reason'])
                augmented_data.append(new_item)

        print(f"Info: Entity swapping generated {len(augmented_data)} new examples")
        return augmented_data

    def sentence_restructuring(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = []

        for item in data:
            new_item = item.copy()
            reason = new_item['reason']

            words = reason.split()
            if len(words) > 3:
                split_point = len(words) // 2
                new_reason = ' '.join(words[split_point:] + words[:split_point])
                new_reason = new_reason.capitalize() + '.'
                new_item['reason'] = new_reason

            augmented_data.append(new_item)

        return augmented_data

    def paraphrase_with_mentor(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = []
        for item in data:
            new_item = item.copy()
            prompt = f"Paraphrase the following sentence while keeping the same meaning and sentiment: '{item['reason']}'"
            paraphrase = self.mentor.predict(system_text=None, text=prompt)
            new_item['reason'] = paraphrase['results'][0]['text']
            augmented_data.append(new_item)
        return augmented_data

    def generate_contrasting_examples(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = []
        for item in data:
            new_item = item.copy()
            opposite_sentiment = "positive" if item['sentiment'] == "negative" else "negative"
            prompt = f"Generate a {opposite_sentiment} sentiment example about {item['entity']} that contrasts with: '{item['reason']}'"
            contrast = self.mentor.predict(system_text=None, text=prompt)
            new_item['sentiment'] = opposite_sentiment
            new_item['reason'] = contrast['results'][0]['text']  # Adjust based on your mentor's output structure
            augmented_data.append(new_item)
        return augmented_data

    def entity_attribute_expansion(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = []
        for item in data:
            new_item = item.copy()
            prompt = f"Provide additional attributes or characteristics of {item['entity']} that are relevant to the sentiment: '{item['sentiment']}'"
            expansion = self.mentor.predict(system_text=None, text=prompt)
            new_item['reason'] += " " + expansion['results'][0][
                'text']
            augmented_data.append(new_item)
        return augmented_data

    def contextual_example_generation(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = []
        for item in data:
            new_item = item.copy()
            prompt = f"Generate a specific example or scenario that illustrates the {item['sentiment']} sentiment towards {item['entity']} based on: '{item['reason']}'"
            example = self.mentor.predict(system_text=None, text=prompt)
            new_item['reason'] = example['results'][0]['text']
            augmented_data.append(new_item)
        return augmented_data

    def sentiment_intensity_variation(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        augmented_data = []
        intensities = ["slightly", "moderately", "very", "extremely"]
        for item in data:
            for intensity in intensities:
                new_item = item.copy()
                prompt = f"Modify the following to express a {intensity} {item['sentiment']} sentiment: '{item['reason']}'"
                variation = self.mentor.predict(system_text=None, text=prompt)
                new_item['reason'] = variation['results'][0]['text']
                augmented_data.append(new_item)
        return augmented_data

    def cross_domain_adaptation(self, data: List[Dict[str, Any]], target_domain: str) -> List[Dict[str, Any]]:
        augmented_data = []
        for item in data:
            new_item = item.copy()
            prompt = f"Adapt the following sentiment analysis from its original domain to the domain of {target_domain}, keeping the same sentiment: Entity: {item['entity']}, Sentiment: {item['sentiment']}, Reason: '{item['reason']}'"
            adaptation = self.mentor.predict(system_text=None, text=prompt)
            adapted_item = adaptation['results'][0]
            new_item['entity'] = adapted_item['entity']
            new_item['reason'] = adapted_item['reason']
            augmented_data.append(new_item)
        return augmented_data

    def generate_test_cases(self, prompts: List[str]) -> List[Dict[str, Any]]:
        test_cases = []
        for prompt in prompts:
            mentor_response = self.mentor.predict(system_text=None, text=prompt)

            # Process the mentor's response using the task's processor
            processed_response = self.task.processor(mentor_response['results'][0]['text'])

            # Validate the processed response using the task's output model
            try:
                validated_response = self.task.output_model(**processed_response)
                test_cases.append(validated_response.dict())
            except ValueError as e:
                print(f"Skipping invalid test case for prompt '{prompt}': {str(e)}")

        return test_cases
