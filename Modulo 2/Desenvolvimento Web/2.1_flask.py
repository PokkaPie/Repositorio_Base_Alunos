from flask import Flask, render_template

app = Flask(__name__) # instanciando o flask

@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/zezinho')
def zezinho():
    return 'Achou a rota'

if __name__ == '__main__':
    app.run(debug=True)