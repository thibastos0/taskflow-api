from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Sistema de Gerenciamento de Biblioteca"

@app.route("/status")
def status():
    return {"status": "API online"}

@app.route("/sobre")
def sobre():
    return "Projeto desenvolvido na disciplina de Integração e Entrega Contínua"

@app.route("/usuarios")
def usuarios():
    return jsonify(["Ana", "Carlos", "Maria", "Thiago"])

if __name__ == '__main__':
    app.run(debug=True)
