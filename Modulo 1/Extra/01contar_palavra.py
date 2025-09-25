texto = input("Digite um texto: ")
palavras = texto.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)