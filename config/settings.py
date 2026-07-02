import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "llama3.1:8b")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))
PDF_PATH = os.getenv("PDF_PATH", "data/pdfs/hr.pdf")
DEBUG = True