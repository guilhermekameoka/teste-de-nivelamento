## Função para salvar o DataFrame em um arquivo CSV
def save_to_csv(df, csv_filename):
    print("Convertendo para CSV...")
    # Converte o DataFrame para CSV (sem o índice) e com codificação UTF-8
    df.to_csv(csv_filename, index=False, encoding="utf-8")
    print(f"Salvando CSV como {csv_filename}...")
