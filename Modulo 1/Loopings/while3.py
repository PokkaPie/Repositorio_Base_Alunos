print("´´´´´´´´´"*8)
n = int(input("DIgite um numero fatorial: "))
result = 1
f = 1
print("´´´´´´´´´"*8)
while f <= n:
    result *= f
    f += 1
    print(f"O fatorial do {n} é : , {result}")
print("´´´´´´´´´"*8)