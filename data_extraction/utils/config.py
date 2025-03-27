import os                       # Biblioteca os para manipulação de caminhos de arquivos
from dotenv import load_dotenv  # Importando o método load_dotenv para carregar variáveis de ambiente de um arquivo .env

# Define o caminho para o arquivo .env na raiz do projeto
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv(dotenv_path)

# Obtém valores das variáveis de ambiente
PDF_PATH = os.getenv("PDF_PATH")
CSV_FILENAME = os.getenv("CSV_FILENAME", "Teste_Guilherme_Kameoka.csv")
ZIP_FILENAME = os.getenv("ZIP_FILENAME", "Teste_Guilherme_Kameoka.zip")
