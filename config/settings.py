import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

TEMPERATURE = float(os.getenv("TEMPERATURE"))