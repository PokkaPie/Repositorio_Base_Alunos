pricompra = input("É a sua primeira compra? (sim/não): ").strip().lower()

totaldacompra = float(input("Qual foi o total da sua compra? R$: "))

if pricompra == "sim" and totaldacompra >= 500:
    print("Voce ganhou um brinde! Seja bem vindo!")
else:
    print("Seja bem vindo!")

