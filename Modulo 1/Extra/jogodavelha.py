from random import rangerange
from click import clear

def exibir_tabuleiro(tabuleiro):
    clear()
    print("+------"*3, "+", sep="")
    for linha in range(3):
        print("|      "*3,"|", sep="")
        for coluna in range(3):
            print("|    " +str(tabular[linha][coluna])+"   ", end="")
            print("|")
            print("       "*3 "+",sep="")
            print("+------"*3 "+",sep="")

def entrada_jogador(tabuleiro):
    valido = False
    while not valido:
        movimento = input("Digite seu movimento: ")
        valido = len(movimento) == 1 and movimento >= "1" and movimento <= "9"
        if not valido:
            print("Movimento ruim - repita seua entrada!")
            continue
        movimento = int(movimento) - 1
        linha = movimento // 3
        coluna = movimento % 3
        conteudo = tabuleiro[linha][coluna]
        valido = conteudo not in ["o", "x"]
        if not valido:
            print("Campo já ocupado - repita sua entrada!")
            continue
        tabuleiro[linha][coluna] = "o"

def lista_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ["o", "x"]
                livres.append((linha, coluna))
    return livres

def verifica_vitoria(tableiro, sinal):
    if sinal == "x":
        vencedor = "computador"
    elif sinal == "o":
        vencedor = "jogador"
    else:
        vencedor = None

    diag1 = diag2 = True
    for i in rage(3)
        if tabuleiro[i][0] == sinal and tabuleiro