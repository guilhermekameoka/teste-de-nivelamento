import os
from dotenv import load_dotenv
from utils import download_file, get_selenium_driver, zip_downloaded_files
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import re
from urllib.parse import urljoin

# Carrega as variáveis de ambiente do arquivo .env e obtém as variáveis necessárias
load_dotenv()
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR")
URL = os.getenv("URL")


def ensure_download_dir():
    """Verifica se o diretório de download já existe. Se não, cria ele."""
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)


# Garante que o diretório de download existe
ensure_download_dir()


def scrape_and_download_files():
    """Faz o scraping da página e baixa os arquivos encontrados."""
    driver = get_selenium_driver()
    if driver is None:
        print("Falha ao iniciar o WebDriver. Abortando...")
        return []

    try:
        driver.get(URL)
        soup = BeautifulSoup(driver.page_source, "html.parser")
    finally:
        driver.quit()  # Fecha o WebDriver após obter o conteúdo

    links = soup.find_all("a", href=True)
    pdf_files = []

    for link in links:
        href = link["href"]
        if re.search(r"Anexo\s*[I|II]", link.text, re.IGNORECASE) and href.endswith(".pdf"):
            full_url = urljoin(URL, href)
            print(f"Arquivo encontrado: {link.text.strip()} ({href})")
            print(f"Baixando arquivo de: {full_url}")
            pdf_files.append(download_file(full_url, DOWNLOAD_DIR))

    return [
        file for file in pdf_files if file
    ]  # Retorna arquivos que foram baixados com sucesso


if __name__ == "__main__":
    print("Iniciando o processo de scraping e download...")
    pdf_files = scrape_and_download_files()

    if pdf_files:
        zip_downloaded_files(pdf_files, "anexos.zip")  # Compacta os arquivos baixados
        print("Processo concluído com sucesso!")
    else:
        print("Nenhum arquivo foi baixado.")