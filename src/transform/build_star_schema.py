# src/transform/build_star_schema.py
import pandas as pd
from utils.io import CURATED

def build_dimensions(facts: pd.DataFrame):
  dim_country = facts[["geoAreaCode","geoAreaName"]].drop_duplicates().rename(
    columns={"geoAreaCode":"country_key","geoAreaName":"country_name"}
  )
  dim_time = facts[["timePeriod"]].drop_duplicates().rename(columns={"timePeriod":"year"})
  dim_indicator = facts[["indicator","indicatorName"]].drop_duplicates().rename(
    columns={"indicator":"indicator_key","indicatorName":"indicator_name"}
  )
  return dim_country, dim_time, dim_indicator

def build_fact(facts: pd.DataFrame):
  cols = ["value","timePeriod","geoAreaCode","indicator"]
  f = facts[cols].rename(columns={
    "value":"measure_value",
    "timePeriod":"year",
    "geoAreaCode":"country_key",
    "indicator":"indicator_key"
  })
  return f

if __name__ == "__main__":
  sdg = pd.read_parquet(CURATED / "sdg_3_2_1.parquet")
  dim_country, dim_time, dim_indicator = build_dimensions(sdg)
  fact = build_fact(sdg)
  dim_country.to_parquet(CURATED / "dim_country.parquet", index=False)
  dim_time.to_parquet(CURATED / "dim_time.parquet", index=False)
  dim_indicator.to_parquet(CURATED / "dim_indicator.parquet", index=False)
  fact.to_parquet(CURATED / "fact_indicator.parquet", index=False)