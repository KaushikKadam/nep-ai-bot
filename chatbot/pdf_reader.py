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

def load_combined_text():
    combined_text = ""
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            combined_text += extract_text_from_pdf(os.path.join(PDF_DIR, filename))
    return combined_text
