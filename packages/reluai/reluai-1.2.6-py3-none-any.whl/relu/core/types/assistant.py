import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse
from .prompt import promptUser

class aiConfig:
    def __init__(self) -> None:
        self.temperature = 1
        self.top_p = 0.95
        self.top_k = 64
        self.max_output_tokens = 8192
        self.response_mime_type = "text/plain"
        self.model_name = "gemini-1.5-flash"
    def __dict__(self) -> dict:
        dicty = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_output_tokens": self.max_output_tokens,
            "response_mime_type": self.response_mime_type,
        }
        return dicty

class relu:
    def __init__(self, data):
        self.key = data.get("key")
        genai.configure(api_key=self.key)
        self.context = data.get("context")
        self.model = genai.GenerativeModel(
            model_name=aiConfig().model_name,
            generation_config=aiConfig().__dict__(),
            system_instruction=self.context,
        )

    def generate(self, prompt:promptUser):
        text = f"""Eres un asistente util llamado ReLU, tienes la siguiente información del usuario:
{prompt.__str__()}

Tienes que responder en base a esa información en especifico, y trata siempre de responder de manera más rápida y analítica, solo pide detalles si es necesario.
El usuario te ha preguntado lo siguiente:

[{prompt.now}] {prompt.user}: {prompt.text}
ReLU: """
        response:GenerateContentResponse = self.model.generate_content(text, stream=True)
        return response