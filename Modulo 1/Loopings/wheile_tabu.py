
print("tabuada de todos os numeros")
numero = 1
while numero <= 10:
    print(f"\n tabela do {numero}:")
    contador = 1
    while contador <= 10 :
        resultado = numero * contador
        print(f"{numero}x{contador}={resultado}")
        contador += 1
    numero += 1