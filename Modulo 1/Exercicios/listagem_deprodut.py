estoque = {}

def exibir_menu():
    print("\n=&= *MENU* =&=")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Realizar venda")
    print("4. Sair")

def cadastrar_produto():
    nome = input("Digite o nome do produto: ").strip().capitalize()
    if nome in estoque:
        print("Produto já cadastrado. Adicionando ao estoque.")
    quantidade = int(input("Digite a quantidade: "))
    estoque[nome] = estoque.get(nome, 0) + quantidade
    print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\n--- Produtos em Estoque ---")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

def realizar_venda():
    nome = input("Digite o nome do produto que deseja vender: ").strip().capitalize()
    if nome not in estoque:
        print("Produto não encontrado no estoque.")
        return
    quantidade = int(input("Digite a quantidade a ser vendida: "))
    if quantidade > estoque[nome]:
        print("Quantidade insuficiente em estoque.")
    else:
        estoque[nome] -= quantidade
        print(f"Venda realizada: {quantidade} unidades de {nome}")
        if estoque[nome] == 0:
            del estoque[nome]

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            realizar_venda()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
