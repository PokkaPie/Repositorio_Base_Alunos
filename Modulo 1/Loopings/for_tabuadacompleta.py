numero = 7
print("tabuada de todos os numeros usando for")
print("#" * 200)
for numero in range (1,11):
    print(f"\n tabuada do{numero}: ")
    print("-"*20)
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero}x{i}={resultado}")
        