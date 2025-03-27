import zipfile  # Biblioteca usada para criar e manipular arquivos ZIP
import os       # Biblioteca usada para manipulação de caminhos e nomes de arquivos


def zip_downloaded_files(pdf_files, zip_path):
    """Recebe uma lista de arquivos PDF e os compacta em um único arquivo ZIP."""
    # Cria um novo arquivo ZIP no caminho especificado
    with zipfile.ZipFile(zip_path, "w") as zipf:
        # Percorre a lista de arquivos para adicioná-los ao ZIP
        for file in pdf_files:
            # Adiciona o arquivo ao ZIP usando apenas seu nome base, sem incluir o caminho completo
            zipf.write(file, os.path.basename(file))
    # Imprime uma mensagem de sucesso informando onde o arquivo ZIP foi salvo
    print(f"Arquivos baixados e compactados em {zip_path}")
