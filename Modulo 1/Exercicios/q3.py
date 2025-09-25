nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota_final = ((nota1 + nota2 + nota3)/3)

print(f"Essa é nota final: {nota_final} ")

if nota_final < 5:
    print("Sua nota é vermelha, reprovado.")
elif nota_final >= 5 <= 6:
    print("Sua nota é mediana.")
elif nota_final > 6:
    print("Sua nota boa.")
else:
    nota_final >= 10
    print("sua nota e incrivel! nota maxima.")
