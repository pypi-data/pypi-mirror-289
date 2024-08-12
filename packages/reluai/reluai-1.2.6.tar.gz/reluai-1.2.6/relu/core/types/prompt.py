from datetime import datetime
import platform
import importlib
import sys
import os

# Añade la ruta del directorio donde está el módulo a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../utils')))

# Importa el módulo por su nombre
configOperations = importlib.import_module('configOperations')

class promptUser:
    def __init__(self, text):
        config = configOperations.load_config()
        self.text:str = text
        self.now:str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user:str = config.get("name", "user")
        self.lenguage:str = config.get("lang", "es")
        self.country:str = None
        self.env:str = "terminal",
        self.os:str = platform.system()
    
    def __str__(self) -> str:
        texto = f"""Username: {self.user}
Hour: {self.now}
Language: {self.lenguage}
Country: {self.country}
Environment: {self.env}
OS: {self.os}"""
        return texto