def search_in_text(text, keyword):
    results = []
    lines = text.splitlines()

    for i, line in enumerate(lines):
        if keyword.lower() in line.lower():
            results.append((i, line.strip()))

    return results