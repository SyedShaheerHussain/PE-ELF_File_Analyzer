from bs4 import BeautifulSoup

def parse_html(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    return {
        "title": soup.title.string if soup.title else "",
        "links": [a.get("href") for a in soup.find_all("a") if a.get("href")],
        "text": soup.get_text()
    }