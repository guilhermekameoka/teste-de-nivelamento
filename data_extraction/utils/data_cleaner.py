import pandas as pd


# Função para limpar e transformar os dados
def clean_and_transform_data(data):
    # Converte os dados recebidos para um DataFrame do pandas
    df = pd.DataFrame(data)

    # Substitui as ocorrências da palavra 'OD' por 'Seg. Odontológica'
    df = df.replace(r"\bOD\b", "Seg. Odontológica", regex=True)

    # Substitui as ocorrências da palavra 'AMB' por 'Seg. Ambulatorial'
    df = df.replace(r"\bAMB\b", "Seg. Ambulatorial", regex=True)

    # Retorna o DataFrame transformado
    return df
