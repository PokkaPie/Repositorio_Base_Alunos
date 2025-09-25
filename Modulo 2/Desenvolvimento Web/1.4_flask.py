from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Mundo!'

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é José e sou um desenvolvedor Python.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá {nome}! Tudo bem?'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do número {numero} é {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)