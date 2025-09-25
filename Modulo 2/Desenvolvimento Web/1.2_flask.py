from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Mundo!'

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é José e sou um desenvolvedor Python.'




if __name__ == '__main__':
    app.run(debug=True)