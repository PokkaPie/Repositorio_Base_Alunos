# Exercício 3.3: Condicionais em templates
# Crie uma rota que envie uma idade e, no template, use if para
# mostrar uma mensagem se a pessoa for maior de idade e outra se for menor de idade.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # primeira página (home ou index)
def index():
    return 'Hello Flask'

@app.route('/sobre') # segunda página
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/idade/<int:idade>') # terceira página
def idade (idade):
    return render_template('ex_3-3.html',idade=idade)

if __name__ == '__main__':
    app.run(debug=True)