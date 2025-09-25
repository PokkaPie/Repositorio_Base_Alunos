# Exer. 2.2: Links entre rotas
# Adicione um menu de navegaçao simples com links 
# para todas as suas rotas(/,/sobre,/saudacao,etc.).
# Passar a variavel atraves do url_for dentro do script
# html: ("{{url_for('saudacao, nome='Joao')}}")
# 'saudacao' é o nome da funcao Python que define a rota.
# nome='Joao' esta passando o valor para a variavel que rota espera (<nome>)

from flask import Flask, render_template

app = Flask(__name__) # instanciando o flask

@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá, {nome}! Seja bem vindo(a)!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    dobro = numero*2
    return f'O dobro de {numero} é {dobro}.'

if __name__ == '__main__':
    app.run(debug=True)