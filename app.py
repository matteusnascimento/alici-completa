from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from backend.ml_modelos import resposta_ia
from backend.database import init_db
import os

app = Flask(__name__, template_folder="backend/templates", static_folder="backend/static")
CORS(app)
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/responder", methods=["POST"])
def responder():
    data = request.get_json()
    pergunta = data.get("mensagem", "")
    resposta = resposta_ia(pergunta)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)