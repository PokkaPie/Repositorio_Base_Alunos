# José Eduardo Bettoni
print("="*70)
print("=== Conversor de Moedas ===")
print("1 - Real para Dólar")
print("2 - Dólar para Real")
print("0 - Sair")
print("="*70)
# Criando um laço de repetição com while
opcao = -1  # valor inicial qualquer, diferente de 0

while opcao != 0:
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Real para Dólar
        real = float(input("Digite o valor em Reais (BRL): "))
        dolar = real / 5.0  # valor fixo do dólar: 1 USD = 5 BRL
        print(f"{real:.2f} BRL equivalem a {dolar:.2f} USD\n")

    elif opcao == 2:
        # Dólar para Real
        dolar = float(input("Digite o valor em Dólares (USD): "))
        real = dolar * 5.0
        print(f"{dolar:.2f} USD equivalem a {real:.2f} BRL\n")

    elif opcao == 0:
        print("Saindo do conversor. Até logo!")

    else:
        print("Opção inválida. Tente novamente.\n")

print("="*70)

#Concluido.