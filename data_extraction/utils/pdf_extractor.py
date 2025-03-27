import pdfplumber  # biblioteca para extrair dados de arquivos PDF


# Função para extrair dados de um arquivo PDF
def extract_data_from_pdf(pdf_path):
    data = []  # Lista onde os dados extraídos do PDF serão armazenados
    try:
        # Abre o arquivo PDF para leitura
        with pdfplumber.open(pdf_path) as pdf:
            # Itera sobre todas as páginas do PDF
            for page in pdf.pages:
                print("Extraindo dados...")
                # Extrai a tabela da página
                table = page.extract_table()
                # Se uma tabela for encontrada, percorre as linhas e extrai os dados
                if table:
                    for row in table:
                        # Substitui as quebras de linha e remove espaços desnecessários das células
                        data.append(
                            [
                                cell.replace("\n", " ").strip() if cell else ""
                                for cell in row
                            ]
                        )
    except Exception as e:
        # Caso ocorra um erro durante o processo, imprime a mensagem de erro
        print(f"Erro ao processar o PDF: {e}")
        return None
    # Retorna os dados extraídos do PDF
    return data
