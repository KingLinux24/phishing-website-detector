import pandas as pd
from pathlib import Path

DATA = Path("data/raw/urls.csv")

def load():
    df = pd.read_csv(DATA)
    required = {"url", "label", "html_path", "screenshot_path"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df.dropna()

if __name__ == "__main__":
    print(load().head())
