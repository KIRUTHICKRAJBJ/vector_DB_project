
import os
from PyPDF2 import PdfReader
from docx import Document

def load_file(file):
    extension = file.name.split('.')[-1]
    if extension == 'pdf':
        reader = PdfReader(file)
        text = "\n".join(page.extract_text() for page in reader.pages)
    elif extension == 'txt':
        text = file.read().decode('utf-8')
    elif extension == 'docx':
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text
    