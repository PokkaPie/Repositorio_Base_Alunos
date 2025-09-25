num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

result1 = num1 + num2
print(f"o resultado da soma é {result1}")

result2 = num1 - num2
print(f"o resultado da subtração é {result2}")

result3 = num1 * num2
print(f"o resultado da multiplicação é {result3}")

result4 = num1 / num2
if result4 == 0:
    print("Não é possivel realizar divisão com 0.")
else:
    print(f"O resultado da divisão é {result4}")