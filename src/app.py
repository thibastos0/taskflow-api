from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Sistema de Gestão de Biblioteca Online"

@app.route("/status")
def status():
    return {"status": "API online"}

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"

@app.route("/autores")
def autores():
    return "lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato do sistema"

@app.route("/cadastro-livro")
def cadastro_livro():
    return "Formulário de cadastro de livros"

@app.route("/usuarios")
def usuarios():
    return jsonify(["Ana", "Carlos", "Maria", "Thiago"])

if __name__ == '__main__':
    app.run(debug=True)
