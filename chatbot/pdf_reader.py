import os
import re
import PyPDF2

PDF_DIR = "data/nep_pdfs"

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def clean_text(text):
    # Remove excessive newlines
    text = re.sub(r'\n+', '\n', text)
    
    # Remove line breaks in the middle of sentences (e.g. broken phrases)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    # Remove unwanted spaces
    text = re.sub(r'\s+', ' ', text)

    # Fix split words like "develop-\nment"
    text = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', text)

    # Remove non-informative lines (optional, customize if needed)
    lines = text.splitlines()
    clean_lines = [line.strip() for line in lines if len(line.strip()) > 30]  # Keep lines with real content
    return '\n\n'.join(clean_lines)

def load_combined_text():
    combined_text = ""
    if not os.path.exists(PDF_DIR):
        print(f"PDF directory '{PDF_DIR}' not found.")
        return ""

    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned = clean_text(raw_text)
            combined_text += cleaned + "\n\n"

    return combined_text.strip()
