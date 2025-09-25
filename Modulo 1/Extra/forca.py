# import random

# def jogar():

#     imprime_mensagem_abertura()
#     palavra_secreta = carrega_palavra_secreta()
#     letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
#     print(letras_acertadas)

#     enforcou = False
#     acertou = False
#     erros = 0

#     while (not enforcou and not acertou):

#         chute = pede_chute()

#         if (chute in palavra_secreta):
#             index = 0
#             for letra in palavra_secreta:
#                 if (chute == letra):
#                     letras_acertadas[index] = letra
#                 index += 1
#         else:
#             erros += 1

#         enforcou = erros == 6
#         acertou = "_" not in letras_acertadas
#         print(letras_acertadas)
    
#     if (acertou):
#         print("Voce ganhou!")
#         print("☆┌─┐　─┐☆")
#         print("│▒│ /▒/")
#         print("│▒│/▒/")
#         print("│▒/▒/─┬─┐")
#         print("│▒│▒|▒│▒│")
#         print("┌┴─┴─┐-┘─┘")
#         print("│▒┌──┘▒▒▒│")
#         print("└┐▒▒▒▒▒▒┌┘")
#         print("└┐▒▒▒▒┌")

#     print("Fim de jogo.")

# def pede_chute():
#     chute = input("Qual a sua letra?")
#     chute = chute.strip().upper()
#     return chute

# def imprime_mensagem_abertura():
#     print("********************************")
#     print("***Bem vindo ao jogo da forca***")
#     print("********************************")
#     print("░░░░░░░░░░░░░░░░░░░░░▄▀░░▌")
#     print("░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌")
#     print("░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌")
#     print("░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌")
#     print("░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█")
#     print("░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄")
#     print("░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄")
#     print("░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐")
#     print("░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌")
#     print("░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄")
#     print("▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀")
#     print("▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄")
#     print("▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀")
#     print("▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄")
#     print("▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀")
#     print("********************************")

# def carrega_palavra_secreta(nome_do_arquivo = r"C:/Users/Aluno_Programador/Desktop/José Eduardo Bettoni/jogo/Atividade29-palavras_forca.txt"):
#     try:
#         arquivo = open(nome_do_arquivo, "r")
#         palavras = []

#         for linha in arquivo:
#             linha = linha.strip()
#             palavras.append(linha)

#         arquivo.close()

#         numero = random.randrange(0, len(palavras))
#         palavra_secreta = palavras[numero].upper()
#         return palavra_secreta
#     except FileNotFoundError:
#         print(f"Arquivo não encontrado: {nome_do_arquivo}")
#         exit()

# def inicializa_letras_acertadas(palavra):
#     return ["_" for letra in palavra]


# if (__name__ == "__main__"):
#     jogar()

import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
        print("☆┌─┐ 　─┐☆")
        print(" │▒│ /▒/")
        print(" │▒│/▒/")
        print(" │▒/▒/─┬─┐")
        print(" │▒│▒|▒│▒│")
        print("┌┴─┴─┐-┘─┘")
        print("│▒┌──┘▒▒▒│")
        print("└┐▒▒▒▒▒▒┌┘")
        print(" └┐▒▒▒▒┌")
    else:
        print("Você perdeu!")
        print(f"a palavra era: {palavra_secreta}")

    print("Fim de jogo.")

def pede_chute():
    chute = input("Qual a sua letra? ").strip().upper()
    return chute

def imprime_mensagem_abertura():
    print("********************************")
    print("** Bem-vindo ao jogo da forca **")
    print("********************************")
    print("10% Loading…")
    print("█▒▒▒▒▒▒▒▒▒")
    print("40%")
    print("███▒▒▒▒▒▒▒")
    print("50%")
    print("█████▒▒▒▒▒")
    print("70%")
    print("███████▒▒▒")
    print("100%")
    print("██████████")
    print("Boa sorte!")

def carrega_palavra_secreta(nome_do_arquivo=r"C:\Users\Aluno_Programador\Desktop\José Eduardo Bettoni\jogo\Atividade29-palavras_forca.txt"):
    try:
        with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
            palavras = [linha.strip() for linha in arquivo if linha.strip()]

        if not palavras:
            print("⚠️ O arquivo está vazio. Adicione palavras e tente novamente.")
            exit()

        numero = random.randrange(0, len(palavras))
        return palavras[numero].upper()

    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {nome_do_arquivo}")
        exit()

def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]

if __name__ == "__main__":
    jogar()