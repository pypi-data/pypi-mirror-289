from ..core.types.prompt import promptUser
from ..core.types.assistant import relu

from google.generativeai.types.generation_types import GenerateContentResponse
from ..utils.parseResponseMD import process_markdown
from ..utils.configOperations import load_config

def response(prompt:promptUser):
    key = load_config().get("key")
    if not key:
        print ("Establece una key primero, con el parámetro --key <key>, consiguelo en: https://aistudio.google.com/app/apikey")
        return None
    response = relu(data={"key": key}).generate(prompt)
    return response

def processResponse(response:GenerateContentResponse):
    strProcessed = process_markdown(response.text)
    print (strProcessed, end="", flush=True)