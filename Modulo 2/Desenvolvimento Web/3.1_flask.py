# Exercicio 3.1 templates com variaveis
# Modifique o template para receber o nome como variavel e exibir "Bem-vindo, {{nome}}"

from flask import Flask, render_template

app = Flask(__name__) # instanciando o flask

@app.route('/')
def index():
    return render_template('ex_3-1.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('ex_3-1.html', nome=nome)

if __name__ == '__name__':
    app.run(debug=True)