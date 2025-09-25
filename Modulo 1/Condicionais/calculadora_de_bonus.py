dias = int(input("Digite dias uteis: "))

valor = float(input("Digite a quantia vendida em reais no mes: "))

bonus = int(input("Valor do Bonus: "))

# calculo dos valores:

# calculo dos dias:
if dias >= 20:
    print ("pode receber o bonus")
else:
    print("infelizmente nao pode receber o bonus...")
    

# calculo do bonus:
resultado = (valor * 3)/100
print(f"{bonus}% de {valor} é {resultado}")