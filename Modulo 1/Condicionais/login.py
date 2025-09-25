usuario_cadastrado = "alemao"
senha_cadastrada = "1945"

nome_usuario = input("Digite seu nome de usuario: ").strip().lower()
senha = input("Digite sua senha: ").strip().lower()

if nome_usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Login bem sucedido! Bem vindo(a)!", nome_usuario)
else:
    print("Nome de usuario ou senha incorreto. Tente novamente.")