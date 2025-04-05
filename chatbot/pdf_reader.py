import os
import PyPDF2

PDF_DIR = "data/nep_pdfs"

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

import re

def load_combined_text():
    with open("data/combined_text.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Clean formatting: merge broken lines, remove weird newlines
    clean_text = re.sub(r'\n+', ' ', raw_text)  # Replace multiple newlines with space
    clean_text = re.sub(r'\s{2,}', ' ', clean_text)  # Replace multiple spaces with one
    clean_text = clean_text.strip()

    return clean_text

