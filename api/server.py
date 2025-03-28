from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permite requisições da interface Vue.js

# Carrega os dados do CSV
csv_path = "/Users/guilhermekameoka/Desktop/prova/database/active_insurance_providers/Relatorio_cadop.csv"
df = pd.read_csv(csv_path, encoding="utf-8", sep=";")

# Rota para o index.html
@app.route("/")
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), "index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify({"error": "Parâmetro de busca vazio"}), 400

    # Filtra os registros que comtém a query (case insensitive)
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
    
    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)