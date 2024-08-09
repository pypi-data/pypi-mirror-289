# AKALI: Aggressive Knowledge Augmenter and Language Interface

<p align="center">
  <img src="assets/logo.jpg" alt="AKALI Logo" width="512"/>
</p>

AKALI is a powerful library for language model augmentation and interfaces, designed to enhance the capabilities of AI models through strategic data augmentation and efficient task management.

## Features

- **Language Interface**: Easily integrate and interact with various language models.
- **Knowledge Augmentation**: Improve model performance through intelligent data augmentation strategies.
- **Task Management**: Flexible system for handling different NLP tasks.
- **CLI Tool**: Command-line interface for easy usage and integration.
- **Customizable**: Extend functionality with custom tasks and augmentation strategies.

## Installation

```bash
pip install akali
```

## Quick Start
Using the CLI tool
Run a language interface service directly
```bash
akali run --model alierenak/gemma-7b-akali --task EntitySentimentReasoner --host 0.0.0.0 --port 8000
```

Make a prediction
```bash
akali predict --model alierenak/gemma-7b-akali --task EntitySentimentReasoner --user-message "Turkcell hiç güzel çeken bir hat değil o yüzden Vodofone'u tercih ediyorum hem de daha ucuz"
```

Using as a Python Library
```python
from akali import LanguageInterface
li = LanguageInterface.load_model("alierenak/gemma-7b-akali")

# Set the task
li.set_task("EntitySentimentReasoner")

# Make a prediction
result = li.predict(system_text=None, user_message="Turkcell hiç güzel çeken bir hat değil o yüzden Vodofone'u tercih ediyorum hem de daha ucuz")
print(result)
```
# Advanced Usage

## Custom Task Creation
```python
from akali import LanguageInterface
from pydantic import BaseModel
from typing import List, Dict, Any

class CustomOutput(BaseModel):
    entity_list: List[str]
    results: List[Dict[str, str]]

def custom_processor(result: str) -> Dict[str, Any]:
    # Your custom processing logic here
    pass

li = LanguageInterface.load_model("your_model_id")
li.set_custom_task("CustomTask", custom_processor, CustomOutput)
```
## Knowledge Augmentation

```python
from akali import LanguageInterface, AggressiveKnowledgeAugmenter, AugmenterConfig

mentee = LanguageInterface.load_model("mentee_model_path")
mentor = LanguageInterface.load_model("mentor_model_path")

config = AugmenterConfig(
    # Configure your augmentation settings
)

augmenter = AggressiveKnowledgeAugmenter(mentee, mentor, "EntitySentimentReasoner", config)

# Evaluate current performance
augmenter.evaluate(test_data)

# Propose augmentation strategies
strategies = augmenter.propose()

# Augment the data
augmented_data = augmenter.augment(train_data)
```

## Project Structure

```
akali/
│
├── src/
│   └── akali/
│       ├── __init__.py
│       ├── aka.py
│       ├── li.py
│       ├── utils.py
│       ├── task_manager.py
│       ├── models/
│       ├── processors/
│       └── ...
│
├── examples/
├── tests/
├── .gitignore
├── pyproject.toml
├── README.md
├── requirements.txt
└── setup.py
```
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is proprietary and confidential. Unauthorized copying, transferring or reproduction of this project, via any medium, is strictly prohibited.

## Contact

For licensing inquiries, support or anything, here is my contact mail: akali@sabanciuniv.edu.





