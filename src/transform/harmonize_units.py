# src/transform/harmonize_units.py
import pandas as pd
from utils.io import RAW, CURATED

def standardize(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
  # Example: ensure numeric, drop nulls, add ISO codes
  df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
  df = df.dropna(subset=[value_col])
  return df

if __name__ == "__main__":
  un = pd.read_json(RAW / "un_sdg_3_2_1.json")
  un_std = standardize(un, "value")
  un_std.to_parquet(CURATED / "sdg_3_2_1.parquet", index=False)