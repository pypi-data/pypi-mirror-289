def welcome():
    text_welcome = (
        "¡Bienvenido al asistente interactivo!\n\n"
        "Puedes usar este asistente para interactuar con nuestro sistema de IA.\n\n"
        "Aquí están los parámetros que puedes usar:\n"
        "  - Configuración de nombre: -n <nombre> o --name <nombre>\n"
        "  - Configuración de clave: -k <clave> o --key <clave>\n"
        "  - Configuración de idioma: -l <idioma> o --language <idioma>\n"
        "  - Limpiar memoria del asistente: -c o --clear\n\n"
        "Si solo quieres chatear, simplemente escribe tu mensaje y presiona Enter."
    )
    print(text_welcome)
