import requests
import os


def download_file(url, folder):
    """Baixa um arquivo da URL especificada e o salva na pasta de destino."""
    try:
        local_filename = os.path.join(folder, url.split("/")[-1])
        with requests.get(url, stream=True, timeout=10) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {url}: {e}")
        return None
