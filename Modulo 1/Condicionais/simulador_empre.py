print("="*50)

nome = input("Digite seu nome: ")
renda_mes = float(input("Digite sua renda mensal: "))

print("="*50)

emprestimo = float(input("Digite o valor do emprestimo: "))
parcelas = float(input("Digite a quantidade de parcelas que voce deseja: "))

valor_parcela = ((emprestimo / parcelas))
print(f"esse é o valor de cada parcela: {valor_parcela}")

print("="*50)

renda_legal = renda_mes * 0.3

if emprestimo < 1000 or emprestimo > 50000:
    resultado = "voce nao esta autorizado para receber um emprestimo neste valor"

elif parcelas < 6 or parcelas > 36:
    resultado = "Emprestimo nao autorizado. quantidade de parcelas invalida"

elif valor_parcela > renda_legal:
    resultado = f"Emprestimo nao autorizado: valor das parcelas"
else:
    resultado = f"Emprestimo autorizado. valor das parcelas: R${valor_parcela:.2f}"

print("\nResltado:")
print(resultado)

print("="*50)