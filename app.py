from datetime import datetime
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/maior_idade/<int:ano>")
def verifica_maior_idade(ano):
    now = datetime.utcnow()
    if (now.year-ano)>=18:
        return jsonify({"idade":now.year-ano,
                        "situacao": "Maior Idade"})
    else:
        return jsonify({"idade":now.year-ano,
                        "situacao": "Menor Idade"})
