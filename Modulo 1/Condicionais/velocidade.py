rodizio = input("Hoje é rodizio do seu carro?(sim/não): ").strip().lower()
velocidade = int(input("Qual foi a velocidade do seu carro?(km?h): "))
limitevelocidade = 60

if rodizio == "sim" and velocidade > limitevelocidade:
    print("Voce esta dirigindo no seu dia de rodizio e esta acima da velocidade permitida")
    print("Voce violou as leis do transito")
elif rodizio == "sim":
    print("Voce esta dirigindo no seu dia de rodizio, MULTA!")
elif velocidade > limitevelocidade:
    print("voce estava acima da velocidade permitida, MULTA!")
else:
    print("tudo certo, obrigado por ser um bom cidadao.")