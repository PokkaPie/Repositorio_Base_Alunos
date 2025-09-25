a = int(input("Digite o valor de a : "))
b = int(input("Digite o valor de b : "))
c = int(input("Digite o valor de c : "))

print(f" Comparações: \n")

print(f"(a > b) e (c == b)= ", (a > b and c == b ), "\n")
print(f"(a < b) e (c > b)= ", (a < b or c > b ), "\n")
print(f"NÃO(a != b) = ", not(a != b), "\n")