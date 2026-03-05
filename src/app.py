from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return {"mensagem": "API funcionando corretamente"}

@app.route("/status")
def status():
    return {"status": "API online"}

@app.route("/usuarios")
def usuarios():
    return jsonify(["Ana", "Carlos", "Maria"])

if __name__ == '__main__':
    app.run(debug=True)
