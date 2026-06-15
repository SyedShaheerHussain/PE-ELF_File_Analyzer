def parse_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return {
            "type": "text",
            "text": f.read()
        }