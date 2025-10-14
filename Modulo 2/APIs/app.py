# instalamos  no terminal o flask com o comando: pip install flask 
# importamos o flask para o arquivo 
from flask import Flask, make_response, jsonify, request
from bd_livros import livros

# Bibliotecas
# jsonify = converte listas, dicionários, etc em arquivos json
# make_response = cria um objeto de resposta HTPP completo, ele não apenas retorna os dados
# mas também permite personalizar cabeçalhos e status code. Essa biblioteca vai transformar
# o Json em resposta HTTP

# Instanciamos o flask, ou seja, tornamos a classe (molde) Flask em um 
# objeto (instanciar)
app = Flask(__name__)  
app.config['JSON_SORT_KEYS']=False


# GET - lista todos os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    return make_response(jsonify(
        mensagem='Lista de Livros',
        dados=livros
    )
)

# GET - Buscar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros:
        if livro.get('id')== id:
            return make_response(jsonify(
                mensagem=f'Livro id {id} encontrado',
                dados = livro
            ))
    return make_response(jsonify(
        mensagem = 'Livro não encontrado'
        ),404)

# POST- Cria novo livro
@app.route('/livros', methods=['POST'])
def create_livro():
    livro = request.json
    livros.append(livro)
    return make_response(jsonify(
        mensagem ='Novo livro adicionado com sucesso.',
        dados=livro
    ),201)

# PUT - Atualiza livro(substitui todos os dados)
@app.route('/livros/<int:id>',methods=['PUT'])
def update_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            novo_livro= request.json
            livro.update(novo_livro)
            return make_response(jsonify(
                mensagem='Livro atualizado com sucesso (PUT)',
                dados=livro
            ))
    return make_response(jsonify(
        mensagem ='Livro não encontrado'
    ),404)    

# PATCH - Atualizar parcialmente livro
@app.route('/livros/<int:id>',methods=['PATCH'])
def patch_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            dados= request.json
            livro.update(dados)
            return make_response(jsonify(
                mensagem= f'Livro id {id} atualizado parcialmente.',
                dados=livro
            ))
    return make_response(jsonify(
        mensagem='Livro não encontrado'),404)

# DELETE - remover livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livros(id):
    for livro in livros:
        if livro.get('id') == id:
            livro.remove(livro)
            return make_response(jsonify(
                mensagem =f'Livro de id {id} foi removido com sucesso.',
                dados=livro
            ))
    return make_response(jsonify(mensagem='Livro não encontrado'),404)    

if __name__ == '__main__':
    app.run(debug=True)