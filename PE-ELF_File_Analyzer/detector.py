import os

def detect_file_type(path):
    ext = os.path.splitext(path)[1].lower()

    if ext in [".exe", ".dll"]:
        return "pe"
    elif ext in [".elf", ".bin", ".out", ""]:
        return "elf"
    elif ext == ".docx":
        return "docx"
    elif ext == ".pdf":
        return "pdf"
    elif ext in [".txt", ".log"]:
        return "text"
    elif ext in [".html", ".htm"]:
        return "html"
    elif ext in [".xlsx"]:
        return "xlsx"
    else:
        return "binary"