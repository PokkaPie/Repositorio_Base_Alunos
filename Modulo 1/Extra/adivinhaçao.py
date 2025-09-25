

import random

def jogar_adivinhacao():
    print("================================")
    print("BEM VINDO AO JOGO DA ADIVINHAÇAO")
    print("================================")

    numero_secreto = random.randint(1, 100)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    while True:
        try:
            nivel = int(input("Defina o nível: "))
            if nivel in [1,2,3]:
                break
            else:
                print("Escolha um nivel valido: (1), (2) ou (3).")
        except ValueError:
            print("Por favor, digite um numero valido.")

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")

        while True:
            try:
                chute = int(input("Digite um numero entre 1 e 100: "))
                if 1 <= chute <= 100:
                    break
                else:
                    print("Número fora do intervalo! Digite um numero entre 1 e 100.")
            except ValueError:
                print("Entrada invalida! Digite um numero inteiro.")
        
        print(f"Voce digitou: {chute}")

        if chute == numero_secreto:
                print(f"Parabens! voce acertou e fez {pontos} pontos!")
        else:
            if chute > numero_secreto:
                    print("Voce errou! O numero que voce chutou é maior que o numero secreto,")
            else:
                    print("Voce errou! O numero que voce chutou é menor que o numero secreto.")
                    
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = max(0, pontos - pontos_perdidos)

    print(f"O numero secreto era {numero_secreto}. Fim de jogo!")

if __name__ == "__main__":
    jogar_adivinhacao()