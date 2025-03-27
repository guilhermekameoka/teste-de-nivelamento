import pdfplumber
import pandas as pd
import zipfile
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Nome do arquivo PDF de entrada (do .env)
pdf_path = os.getenv("PDF_PATCH")

# Verificação para garantir que o caminho do arquivo PDF foi carregado corretamente
if not pdf_path or not os.path.exists(pdf_path):
    print(f"Erro: O arquivo {pdf_path} não foi encontrado ou o caminho está incorreto.")
else:
    # Nome do arquivo CSV e ZIP de saída
    csv_filename = "Teste_Guilherme_Kameoka.csv"
    zip_filename = "Teste_Guilherme_Kameoka.zip"

    # Lista para armazenar os dados extraídos
    data = []

    # Função para limpar o texto extraído
    def clean_text(text):
        return text.replace("\n", " ").strip()

    # Extração dos dados do PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    data.append([clean_text(cell) if cell else "" for cell in row])

    # Criar um DataFrame do Pandas
    df = pd.DataFrame(data)

    # Substituir as abreviações OD e AMB
    df = df.replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"})

    # Salvar os dados em CSV
    df.to_csv(csv_filename, index=False, encoding="utf-8")

    # Compactar o arquivo CSV em um ZIP
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)

    # Remover o arquivo CSV original após compactação
    os.remove(csv_filename)

    print(f"Transformação concluida. Arquivo salvo como {zip_filename}.")
