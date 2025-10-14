import requests

cep = input("Digite o CEP (somente números): ")

url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro: {dados['logradouro']}')
        print(f'Bairro: {dados['bairro']}')
        print(f'Cidade: {dados['localidade']}')
        print(f'Estado: {dados['uf']}')
    else:
        print('CEP não foi encontrado')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)
