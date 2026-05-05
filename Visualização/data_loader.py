import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    # Lê o arquivo CSV e converte em DataFrame
    df = pd.read_csv(path, encoding="utf-8-sig")

    # Remove espaços extras nos nomes das colunas
    df.columns = df.columns.str.strip()

    # Converte a coluna 'data' de texto para o tipo datetime
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    # Cria coluna auxiliar com o período no formato AAAA-MM
    df["month_year"] = df["data"].dt.to_period("M").astype(str)

    return df
