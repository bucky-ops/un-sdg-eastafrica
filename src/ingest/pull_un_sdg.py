# src/ingest/pull_un_sdg.py
import requests
import pandas as pd
from utils.io import RAW

BASE = "https://unstats.un.org/SDGAPI/v1/sdg/Indicator/Data"
PARAMS = {"indicator": "3.2.1", "areaCode": "404"}  # Kenya example

def fetch_indicator(indicator_code: str, area_code: str | None = None) -> pd.DataFrame:
  params = {"indicator": indicator_code}
  if area_code:
    params["areaCode"] = area_code
  r = requests.get(BASE, params=params, timeout=60)
  r.raise_for_status()
  data = r.json().get("data", [])
  return pd.DataFrame(data)

if __name__ == "__main__":
  df = fetch_indicator("3.2.1")  # Under-5 mortality rate
  out = RAW / "un_sdg_3_2_1.json"
  df.to_json(out, orient="records", lines=False)
  print(f"Saved {len(df)} rows to {out}")