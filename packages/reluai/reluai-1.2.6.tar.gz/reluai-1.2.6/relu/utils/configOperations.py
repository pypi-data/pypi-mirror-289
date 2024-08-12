import os
import json

# Ruta del archivo de configuración
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

def load_config():
    """Carga la configuración desde el archivo JSON, si existe."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_config(config):
    """Guarda la configuración en el archivo JSON."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def ruta():
    """Devuelve la ruta absoluta del archivo actual."""
    return os.path.abspath(__file__)

def setName(name: str):
    """Configura el nombre en el archivo de configuración y lo imprime."""
    config = load_config()
    config['name'] = name
    save_config(config)
    print(f"Nombre configurado: {name}")

def setKey(key: str):
    """Configura la clave en el archivo de configuración."""
    config = load_config()
    config['key'] = key
    save_config(config)
    print(f"Clave configurada: {key}")

def setlang(lang: str):
    """Configura el idioma en el archivo de configuración."""
    config = load_config()
    config['language'] = lang
    save_config(config)
    print(f"Idioma configurado: {lang}")