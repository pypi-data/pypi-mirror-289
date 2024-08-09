import torch
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, DataCollatorForSeq2Seq
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer
from bitsandbytes import BitsAndBytesConfig


class SFTuning:
    def __init__(self, system_message, model_name, output_dir, token=None):
        self.model_name = model_name
        self.output_dir = output_dir
        self.token = token
        self.tokenizer = None
        self.model = None
        self.trainer = None
        self.system_message = system_message

    def load_model_and_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, token=self.token)
        self.tokenizer.padding_side = 'right'

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map={"": 0},
            token=self.token,
            quantization_config=bnb_config
        )

    def prepare_data(self, texts, labels):
        dataset = Dataset.from_dict({"text": texts, "labels": labels})

        def tokenize_function(examples):
            conversations = [
                f"<start_of_turn>user\n{self.system_message.format(text=text)}<end_of_turn>\n"
                f"<start_of_turn>model\n{label}<end_of_turn>"
                for text, label in zip(examples["text"], examples["labels"])
            ]
            return self.tokenizer(conversations, truncation=True, padding=False)

        tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)
        tokenized_dataset.set_format("torch")
        return tokenized_dataset

    def setup_peft(self):
        peft_config = LoraConfig(
            r=8,
            lora_alpha=32,
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM",
            target_modules=["q_proj", "v_proj"]
        )
        self.model = get_peft_model(self.model, peft_config)

    def train(self, train_dataset, training_args=None):
        if training_args is None:
            training_args = {}

        training_args = TrainingArguments(
            output_dir=self.output_dir,
            **training_args
        )

        data_collator = DataCollatorForSeq2Seq(
            self.tokenizer, pad_to_multiple_of=8, return_tensors="pt", padding=True
        )

        self.trainer = SFTTrainer(
            model=self.model,
            train_dataset=train_dataset,
            peft_config=self.setup_peft(),
            dataset_text_field="text",
            max_seq_length=None,
            tokenizer=self.tokenizer,
            args=training_args,
            packing=False,
            data_collator=data_collator,
        )

        self.trainer.train()

    def save_model(self, push_to_hub=False, repo_name=None):
        self.trainer.model.save_pretrained(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)

        if push_to_hub and repo_name:
            self.trainer.push_to_hub(repo_name, use_auth_token=self.token)