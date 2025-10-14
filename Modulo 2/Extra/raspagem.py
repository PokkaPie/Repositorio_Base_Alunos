import requests
import json
import pyautogui
import time
from bs4 import BeautifulSoup

# 1. Url da página
url ="https://en.wikipedia.org/wiki/Python_(programming_language)"

# 2. Faz a requisição HTTP
response = requests.get(url)
response.encoding ='utf-8'

# 3. Use o Beautifulsoup para parsear o HTML
soup = BeautifulSoup(response.text,"html.parser" )

# 4. Extrair título e primeiro parágrafo
titulo = soup.title.string
primeiro_paragrafo = soup.find('p').text

# # 5.Exibir o título e o primeiro parágrafo
# print(f'Título: {titulo}')
# print(f'Primeiro Parágrafo: {primeiro_paragrafo}')

# 5. Montar um dicionário Python
dados ={
    "titulo":titulo,
    "primeiro_paragrafo":primeiro_paragrafo
}

# 6. Converte para Json
dados_json = json.dumps(dados, indent=4, ensure_ascii=False)

# 7. Salvar em arquivo Json

with open('wikipedia_python.json', 'w', encoding='utf-8') as f:
    f.write(dados_json)

# 8. Pyautogui imprime no terminal
print("Abra o terminal e posicione o cursor, a digitação começa em 5 segundos ...")
time.sleep(5)
pyautogui.write(dados_json, interval=0.01)


