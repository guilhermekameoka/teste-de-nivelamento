import zipfile  # biblioteca para manipulação de arquivos ZIP
import os  # biblioteca para manipulação de arquivos e diretórios


# Função para compactar um arquivo CSV em um arquivo ZIP
def compress_to_zip(csv_filename, zip_filename):
    print(f"Compactando para {zip_filename}...")
    # Cria um arquivo ZIP no modo escrita e utiliza compressão deflacionada
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o arquivo CSV ao arquivo ZIP
        zipf.write(csv_filename)
    # Remove o arquivo CSV original após a compactação
    os.remove(csv_filename)
    print(f"Transformação concluída. Arquivo salvo como {zip_filename}.")
