import pdfplumber

def extract_data_from_pdf(pdf_path):
    data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                print("Extraindo dados...")
                table = page.extract_table()
                if table:
                    for row in table:
                        data.append([cell.replace("\n", " ").strip() if cell else "" for cell in row])
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None
    return data