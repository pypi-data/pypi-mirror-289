from relu.utils.processArgs import main

lista_prompts = [
    "relu",
    "relu Hola mundo",
    "relu --key APIKEY",
    "relu -k APIKEY",
    "relu --name Pedro",
    "relu -n pedro",
    "relu -c"
]

for prompt in lista_prompts:
    print (main(prompt.split()))