from pdfminer.high_level import extract_text

def parse_pdf(path):
    text = extract_text(path)

    pages = text.split("\f")

    return {
        "pages": pages,
        "full_text": text
    }