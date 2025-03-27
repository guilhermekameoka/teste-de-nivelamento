import pandas as pd

def clean_and_transform_data(data):
    df = pd.DataFrame(data)
    df = df.replace(r"\bOD\b", "Seg. Odontológica", regex=True)
    df = df.replace(r"\bAMB\b", "Seg. Ambulatorial", regex=True)
    return df