from .pdf_loader import load_pdf
from .docx_loader import load_docx
from .ppt_loader import load_ppt
from .excel_loader import load_excel
from .txt_loader import load_txt
import os

def load_document(file):
    ext = os.path.splitext(file.name)[1].lower()

    if ext == ".pdf":
        return load_pdf(file)
    elif ext == ".docx":
        return load_docx(file)
    elif ext == ".pptx":
        return load_ppt(file)
    elif ext in [".xls", ".xlsx"]:
        return load_excel(file)
    elif ext == ".txt":
        return load_txt(file)
    else:
        raise ValueError("Unsupported file type")
