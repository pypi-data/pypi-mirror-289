from ..core import aiResponse
from ..core.types import prompt
from ..core.aiResponse import processResponse

from ..utils import printer

from . import configOperations

def main(args: list):
    # Verifica si solo hay un parámetro (inicio)
    if len(args) == 1:
        printer.welcome()

    else:
        args.pop(0)

        PARAMETROS = {
            "name": ["-n", "--name", "-name"],
            "key": ["-k", "--key", "-key"],
            "idioma": ["-l", "--language", "-language"],
            "clear": ["-c", "-clear", "--clear"]
        }
        
        # Verifica si el primer argumento es una opción de configuración
        if args[0].startswith("-"):
            PARAM = args.pop(0)
            VALUE = args.pop(0) if len(args) > 0 else "No especificado"

            if PARAM in PARAMETROS["name"]:
                configOperations.setName(VALUE)
            elif PARAM in PARAMETROS["key"]:
                configOperations.setKey(VALUE)
            elif PARAM in PARAMETROS["idioma"]:
                configOperations.setlang(VALUE)
            elif PARAM in PARAMETROS["clear"]:
                configOperations.clear()
            else:
                print("Parámetro desconocido. Usa -h para ver las opciones disponibles.")

        # Caso en el que no se trata de configuración
        else:
            PROMPT = " ".join(args)
            userPrompt = prompt.promptUser(text=PROMPT)

            response = aiResponse.response(userPrompt)
            if response:
                for chunk in response:
                    processResponse(chunk)
