
estoque_loja = {}

estoque_loja["P001"]={"descrição": "camiseta basica",
                      "preço":39.90,
                      "estoque": {"P":{"preto":10, "azul":5},
                                  "M": {"preto":7, "vermelho":4},
                                  "G":{"preto":3}
                                  }
                                  }
def consultar_estoque(codigo, tamanho, cor):
    produto = estoque_loja.get(codigo)
    if not produto:
        print("Produto não encontrado")
        return
    estoque = produto["estoque"]
    if tamanho in estoque and cor in estoque[tamanho]:
        quantidade = estoque[tamanho][cor]
        print(f"Estoque disponivel de {produto["descrição"]}tamanho:{tamanho}cor:{cor} {quantidade}unidades.")
    else:
        print(f"Produto{codigo} não possui o tamanho {tamanho} ou a cor:{cor} {quantidade} unidades.")

# consultar_estoque("P002","M","preto")
# consultar_estoque("P001","M","preto")
consultar_estoque("P001","G","vermelho")
