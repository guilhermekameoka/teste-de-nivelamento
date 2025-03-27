import zipfile
import os


def zip_downloaded_files(pdf_files, zip_path):
    """Compacta os arquivos baixados em um arquivo ZIP."""
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in pdf_files:
            zipf.write(file, os.path.basename(file))
    print(f"Arquivos baixados e compactados em {zip_path}")
