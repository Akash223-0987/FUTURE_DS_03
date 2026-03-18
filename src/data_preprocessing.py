import pandas as pd
import numpy as np
import os

RAW_PATH = "data/raw/lead_scoring.csv"
PROCESSED_DIR = "data/processed"

def load_data():
    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError(f"Dataset not found at {RAW_PATH}")
    
    # Load and immediately replace "Select" placeholders with NaN
    df = pd.read_csv(RAW_PATH).replace("Select", np.nan)
    return df

def clean(df):
    # Drop high-null columns (>40%)
    limit = 0.40
    null_pct = df.isnull().mean()
    to_drop = null_pct[null_pct > limit].index.tolist()
    df = df.drop(columns=to_drop)
    
    # Simple imputation: Median for numbers, Mode for categories
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(exclude=np.number).columns
    
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    return df.drop_duplicates()

def run():
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df = load_data()
    df = clean(df)
    print(f"[OK] Preprocessed: {df.shape[0]} rows | {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    run()
