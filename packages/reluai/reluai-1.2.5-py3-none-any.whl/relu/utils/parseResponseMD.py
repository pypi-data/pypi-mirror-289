import re

# Secuencias ANSI
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"
CODE = "\033[38;5;28m"
BLOCK_CODE = "\033[48;5;235m\033[38;5;28m"
HEADER1 = "\033[1m\033[38;5;34m"
HEADER2 = "\033[1m\033[38;5;36m"

def process_markdown(content:str):

    content = re.sub(r'^# (.*)$', f'{HEADER1}\\1{RESET}', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.*)$', f'{HEADER2}\\1{RESET}', content, flags=re.MULTILINE)
    content = re.sub(r'```(.*?)```', f'{BLOCK_CODE}\\1{RESET}', content, flags=re.DOTALL)
    content = re.sub(r'\*\*(.*?)\*\*', f'{BOLD}\\1{RESET}', content)
    content = re.sub(r'\*(.*?)\*', f'{ITALIC}\\1{RESET}', content)
    content = re.sub(r'`(.*?)`', f'{CODE}\\1{RESET}', content)

    return content