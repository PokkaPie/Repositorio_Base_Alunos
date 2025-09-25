usuario_cadastrado = "Samuel"
senha_cadastrada = "senha135"

nome_usuario = input("Digite seu nome de usuario: ").strip().lower()
senha = input("Digite sua senha: ").strip().lower()

if nome_usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Está OK!", nome_usuario)
else:
    print("Nome de usuario ou senha incorreto. Tente novamente.")