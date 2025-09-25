# L
# 10
# 12
# 14
# 16
# 18

idade = int(input("Qual a sua idade? "))

if idade < 10:
    print("Voce apenas pode assistir conteudos com classificaçao livre.")
elif idade >10 and idade <=12:
    print("Voce apenas pode assistir conteudos com classificaçao para menores de 12 anos>")
elif idade >12 and idade <=14:
    print("Voce apenas pode assistir conteudos com classificaçao para menores de 14 anos>")
elif idade >14 and idade <=16:
    print("Voce apenas pode assistir conteudos com classificaçao para menores de 16 anos>")
elif idade >16 and idade <=18:
    print("Voce apenas pode assistir conteudos com classificaçao para menores de 18 anos>")
else:
    print("Voce pode assistir a conteudos com qualquer classificaçao etaria")