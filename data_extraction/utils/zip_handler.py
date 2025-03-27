import zipfile
import os

def compress_to_zip(csv_filename, zip_filename):
    print(f"Compactando para {zip_filename}...")
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)
    os.remove(csv_filename)
    print(f"Transformação concluída. Arquivo salvo como {zip_filename}.")