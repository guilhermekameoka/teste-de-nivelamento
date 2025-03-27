import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

PDF_PATH = os.getenv("PDF_PATH")
CSV_FILENAME = os.getenv("CSV_FILENAME", "Teste_Guilherme_Kameoka.csv")
ZIP_FILENAME = os.getenv("ZIP_FILENAME", "Teste_Guilherme_Kameoka.zip")