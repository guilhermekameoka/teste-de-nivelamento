from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from flask_cors import CORS
import os
from dotenv import load_dotenv
from mangum import Mangum  # Adaptador para rodar Flask na AWS Lambda

# Carrega variáveis do ambiente
load_dotenv()

app = Flask(__name__)
CORS(app)  # Permite requisições da interface Vue.js

# Carrega os dados do CSV
csv_path = os.getenv("CSV_PATH")
df = pd.read_csv(csv_path, encoding="utf-8", sep=";")


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()
    limit = int(request.args.get("limit", 10))  # Limite de resultados

    if not query:
        return jsonify({"error": "Parâmetro de busca vazio"}), 400

    # Filtra os registros que contêm a query (case insensitive)
    results = df[
        df.apply(
            lambda row: row.astype(str).str.contains(query, case=False, na=False).any(),
            axis=1,
        )
    ]

    # Limita o número de resultados
    results = results.head(limit)

    print("Dados retornados do servidor:", results.to_dict(orient="records"))  # Log

    return jsonify(results.to_dict(orient="records"))

# Adaptador para AWS Lambda
lambda_handler = Mangum(app)