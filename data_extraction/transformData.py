import os
from data_extraction.utils.config import PDF_PATH, CSV_FILENAME, ZIP_FILENAME
from data_extraction.utils.pdf_extractor import extract_data_from_pdf
from data_extraction.utils.data_cleaner import clean_and_transform_data
from data_extraction.utils.csv_handler import save_to_csv
from data_extraction.utils.zip_handler import compress_to_zip

if not PDF_PATH or not os.path.exists(PDF_PATH):
    print(f"Erro: O arquivo {PDF_PATH} não foi encontrado ou o caminho está incorreto.")
    exit(1)

print(f"Lendo PDF: {PDF_PATH}")
data = extract_data_from_pdf(PDF_PATH)

if data is None:
    exit(1)

df = clean_and_transform_data(data)
save_to_csv(df, CSV_FILENAME)
compress_to_zip(CSV_FILENAME, ZIP_FILENAME)
