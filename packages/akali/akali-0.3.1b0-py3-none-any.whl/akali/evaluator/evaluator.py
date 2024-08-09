from typing import List, Dict, Any

import matplotlib.pyplot as plt
import numpy as np


class Evaluator:
    def __init__(self, comparison_criteria, config):
        self.comparison_criteria = comparison_criteria
        self.config = config

    def analyze_results(self, results: List[Dict[str, Any]]) -> Dict[str, float]:
        strategy_scores = {strategy: 0.0 for strategy in self.config.augmentation_strategies}
        total_examples = len(results)
        metrics = {metric: [] for metric in self.config.metric_extractors}

        for result in results:
            cr = result['comparison_result']
            for metric, extractor in self.config.metric_extractors.items():
                metrics[metric].append(extractor(cr))

        avg_metrics = {metric: sum(values) / len(values) for metric, values in metrics.items()}
        for strategy, condition in self.config.strategy_conditions.items():
            strategy_scores[strategy] = condition(avg_metrics)

        for strategy in strategy_scores:
            strategy_scores[strategy] /= total_examples

        strategy_scores = self.config.score_adjustments(strategy_scores, avg_metrics)
        return strategy_scores

    @staticmethod
    def generate_report(initial_eval: Dict[str, List[Dict[str, Any]]],
                        final_eval: Dict[str, List[Dict[str, Any]]],
                        augmentation_stats: Dict[str, int]) -> None:
        # Prepare data
        initial_scores = [r['comparison_result']['overall_accuracy'] for r in initial_eval['results']]
        final_scores = [r['comparison_result']['overall_accuracy'] for r in final_eval['results']]

        # Plot performance improvement
        plt.figure(figsize=(10, 6))
        plt.boxplot([initial_scores, final_scores], labels=['Initial', 'After Augmentation'])
        plt.title('Model Performance Before and After Augmentation')
        plt.ylabel('Overall Accuracy')
        plt.savefig('performance_improvement.png')
        plt.close()

        strategies = list(augmentation_stats.keys())
        counts = list(augmentation_stats.values())
        plt.figure(figsize=(10, 6))
        plt.bar(strategies, counts)
        plt.title('Augmentation Strategy Usage')
        plt.xlabel('Strategy')
        plt.ylabel('Number of Examples Generated')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('augmentation_strategy_usage.png')
        plt.close()

        summary = {
            'Initial Mean Accuracy': np.mean(initial_scores),
            'Final Mean Accuracy': np.mean(final_scores),
            'Improvement': np.mean(final_scores) - np.mean(initial_scores),
            'Total Augmented Examples': sum(augmentation_stats.values())
        }

        # Save summary to file
        with open('augmentation_report.txt', 'w') as f:
            for key, value in summary.items():
                f.write(f"{key}: {value}\n")

        print(
            "Report generated. Check 'performance_improvement.png',"
            "'augmentation_strategy_usage.png', and 'augmentation_report.txt'."
        )