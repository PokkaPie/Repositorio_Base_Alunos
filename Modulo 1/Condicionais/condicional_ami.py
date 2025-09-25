print("Sistema de Classificação por idade")
print(""*30)

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("ERR0: Idade não pode ser (-)")
else:
    if idade < 12:
        print("Você uma criança.")
        if idade <= 5:
            print("Pré-adolescente")
        else:
            print("Pré adolescente.")
    elif idade < 18:
        print("Voce e um adolescente.")
        if idade < 15:
            print("Adolescente inicial.")
        else:
            print("Adolescente tardia.")
    elif idade <60:
        print("vc Adulto.")
        if idade < 30:
            print("Adulto jovem")
        elif idade < 45:
            print("Adulto")
        else:
            print("Adulto maduro.")
    else:
        print("Voce e idoso.")
        if idade < 75:
            print("Terceira idade.")
        else:
            print("Quarta idade.")
