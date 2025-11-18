# src/utils/io.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
RAW = Path(os.getenv("DATA_DIR_RAW", "./data_raw"))
CURATED = Path(os.getenv("DATA_DIR_CURATED", "./data_curated"))
RAW.mkdir(exist_ok=True)
CURATED.mkdir(exist_ok=True)