# 1. Função para calcular o combustível necessário
def calcular_combustivel(distancia, consumo):
    litros = distancia / consumo
    return litros

# 2. Função para calcular o custo da viagem
def calcular_custo(litros, preco_combustivel):
    custo = litros * preco_combustivel
    return custo

# 3. Função para verificar se o dinheiro disponível é suficiente
def verificar_dinheiro(custo, dinheiro_disponivel):
    if dinheiro_disponivel >= custo:
        return "Você tem dinheiro suficiente."
    else:
        return "Você NÃO tem dinheiro suficiente."
