import requests     # A biblioteca `requests` é usada para fazer requisições HTTP
import os           # A biblioteca `os` é usada para manipular diretórios e arquivos no sistema operacional


def download_file(url, folder):
    """Baixa um arquivo da URL especificada e o salva na pasta de destino."""
    try:
        # Determina o nome do arquivo local a partir da URL
        local_filename = os.path.join(folder, url.split("/")[-1])
        # A requisição HTTP é feita e os dados são baixados em chunks para eficiência
        with requests.get(url, stream=True, timeout=10) as r:
            # Verifica se houve erro na requisição
            r.raise_for_status()
            # O arquivo será salvo no modo binário
            with open(local_filename, "wb") as f:
                # Os dados são gravados em pedaços para evitar uso excessivo de memória
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename
    # Captura erros da requisição e exibe uma mensagem de erro
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {url}: {e}")
        return None