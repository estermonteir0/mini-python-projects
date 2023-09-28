with open('story.txt', 'r') as f:
    historia = f.read()

palavras = set()
inicio_da_palavra = -1

inicio_alvo = '<'
fim_alvo = '>'

for i, carac in enumerate(historia):
    if carac == inicio_alvo:
        inicio_da_palavra = i

    if carac == fim_alvo and inicio_da_palavra != -1:
        palavra = historia[inicio_da_palavra: i + 1]
        palavras.add(palavra)
        inicio_da_palavra = -1

respostas = {}

for palavra in palavras:
    resposta = input('Entre com uma palavra para ' + palavra + ': ')
    respostas[palavra] = resposta

for palavra in palavras:
    historia = historia.replace(palavra, respostas[palavra])

print(historia)