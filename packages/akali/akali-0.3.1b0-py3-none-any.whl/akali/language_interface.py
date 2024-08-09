import nest_asyncio
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Callable, Type, Dict, Any
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from .task_manager import TaskManager, Task


class InputModel(BaseModel):
    text: str
    system_text: Optional[str] = None
    is_gemma_esr: Optional[bool] = True


class LanguageInterface:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.app = None
        self.task: Optional[Task] = None

    @classmethod
    def load_model(
            cls,
            model_id_or_path: str,
            quantization: Optional[str] = None,
            hf_token: Optional[str] = None,
    ):
        interface = cls()

        interface.tokenizer = AutoTokenizer.from_pretrained(
            model_id_or_path,
            token=hf_token,
        )

        if quantization:
            if quantization not in ["4bit", "8bit"]:
                raise ValueError("Quantization must be either '4bit' or '8bit'")

            quantization_config = BitsAndBytesConfig(
                load_in_4bit=(quantization == "4bit"),
                load_in_8bit=(quantization == "8bit")
            )
            interface.model = AutoModelForCausalLM.from_pretrained(
                model_id_or_path,
                quantization_config=quantization_config,
                device_map="auto",
                token=hf_token,
            )
        else:
            interface.model = AutoModelForCausalLM.from_pretrained(
                model_id_or_path,
                token=hf_token,
            ).to(interface.device)

        return interface

    def set_task(self, task: str):
        self.task = TaskManager.get_task(task)

    def set_custom_task(self, name: str, processor: Callable, output_model: Type[BaseModel]):
        self.task = Task(name=name, processor=processor, output_model=output_model)

    def predict(self, text: str, system_text: Optional[str] = None, is_gemma_esr=True) -> Dict[str, Any]:
        if not self.task:
            raise RuntimeError("Task not set. Call set_task() first.")

        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")

        if is_gemma_esr:
            formatted_prompt = f"""<start_of_turn>user
            Sen, varlık duygu analizi konusunda uzmanlaşmış bir yapay zeka asistanısın. Görevin, verilen Türkçe metindeki varlıkları (kişi, şirket, ürün vb.) belirlemek, her varlıkla ilişkili duyguyu tespit etmek ve duygunun kısa bir nedenini sunmaktır. Aşağıdaki girdideki varlıkların duygularını bu formatta analiz et!
            Girdi: {text} <eos><end_of_turn>
            <start_of_turn>model
            """
        else:
            messages = [
                {"role": "user", "content": text},
            ]
            if system_text:
                messages.insert(0, {"role": "system", "content": system_text})
            formatted_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False)

        input_ids = self.tokenizer(formatted_prompt, return_tensors="pt").input_ids.to(self.device)
        input_length = input_ids.shape[1]

        with torch.no_grad():
            outputs = self.model.generate(input_ids, max_new_tokens=1000)

        result = self.tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
        processed_result = self.task.processor(result)

        try:
            return self.task.output_model(**processed_result).dict()
        except ValueError as e:
            raise ValueError(f"Output validation failed: {str(e)}")

    def setup_routes(self):
        @self.app.post("/predict/")
        async def predict_endpoint(item: InputModel):
            try:
                return self.predict(text=item.text, system_text=item.system_text, is_gemma_esr=item.is_gemma_esr)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    def run_service(self, host: str, port: int, run_async=False):
        self.app = FastAPI()
        self.setup_routes()
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        if not self.task:
            raise RuntimeError("Task not set. Call set_task() first.")

        try:
            if run_async:
                nest_asyncio.apply()
                print("LOGGING: nest_asyncio applied. Running server in async mode.")
        except ImportError:
            print("LOGGING: nest_asyncio not installed. Running server in sync mode.")

        uvicorn.run(self.app, host=host, port=port)