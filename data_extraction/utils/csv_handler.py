def save_to_csv(df, csv_filename):
    print("Convertendo para CSV...")
    df.to_csv(csv_filename, index=False, encoding="utf-8")
    print(f"Salvando CSV como {csv_filename}...")