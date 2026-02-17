from pypdf import PdfReader

def load_resume(pdf_path: str) -> str:

    reader = PdfReader(pdf_path)
    pages = reader.pages
    text = ""
    for page in pages:
        extract = page.extract_text()
        if extract is not None:
            text += extract
    return text

test = load_resume('CoverLetter.pdf')
print(test)