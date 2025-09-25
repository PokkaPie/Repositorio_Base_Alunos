#José Eduardo Bettoni

#CODIGO ORIGINAL:

# nome = input("Qual é o seu nome?: ")
# idade = int(input("Qual a sua idade?: "))
# possui_carteira = input("Possui CNH? \n (1-Sim/ 2-Não): ")

# if idade >= 18:
#     if possui_carteira == "1":
#         print("DIRIJA IMEDIATAMENTE!")
#     else:
#         print("NAO DIRIJA!")
# else:
#     print("VOCE NAO PODE DIRIGIR, IDADE INDEVIDA!")

#CODIGO OTIMIZADO:

# Adicionei uma função ao codigo para uma verificação mais adequada utilizando o ("def + ()")
def verificar_habilitacao():
    nome = input("Qual é o seu nome?: ")

    # Validação da idade / adicionei um identificador de erros
    while True:
        try:
            idade = int(input("Qual a sua idade?: "))
            break
        except ValueError:
            print("Por favor, digite uma idade válida (número inteiro).")

    # Validação da CNH / adicionei um ("while") e um ("break") para mais variações
    while True:
        possui_carteira = input("Possui CNH? (1 - Sim / 2 - Não): ")
        if possui_carteira in ("1", "2"):
            break
        else:
            print("Opção inválida. Digite 1 para 'Sim' ou 2 para 'Não'.")

    # Lógica principal / adicionei um novo ("if") para detectar mais variáveis
    if idade >= 18:
        if possui_carteira == "1":
            print(f"{nome}, você pode dirigir IMEDIATAMENTE!")
        else:
            print(f"{nome}, você TEM idade, mas NÃO pode dirigir sem CNH!")
    else:
        print(f"{nome}, você NÃO pode dirigir, IDADE INDEVIDA!")

# Executa a função
verificar_habilitacao()
