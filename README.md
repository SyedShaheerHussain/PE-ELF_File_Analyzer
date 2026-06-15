# 🧠 Universal File Analyzer v4 PRO

A powerful **reverse engineering + forensic file analysis tool** built with Python and PySide6.  
This tool allows users to analyze **executables, documents, and multiple file types** in a single modern GUI.

Created by: **Syed Shaheer Hussain**  
GitHub: https://github.com/syedshaheerhussain

---

# 🚀 Introduction

The **Universal File Analyzer v4 PRO** is an advanced desktop application designed for:

- Reverse Engineering
- Malware Analysis
- File Forensics
- Document Inspection
- Binary Structure Analysis

It combines multiple analysis engines into a single interface supporting both **binary files and document formats**.

---

# 🎯 Objectives

- Provide a unified file analysis platform
- Support multiple file formats
- Display deep internal file structures
- Help learners understand reverse engineering
- Provide entropy-based security analysis
- Offer a modern GUI experience

---

# 💡 Key Concepts

- File parsing (PE / ELF / Documents)
- Binary analysis
- Entropy calculation (malware detection)
- Strings extraction
- Hexadecimal analysis
- Tree-based structure visualization
- GUI development with PySide6

---

# 🛠 Languages & Technologies Used

- Python 3.x
- PySide6 (Qt GUI Framework)
- PEfile (Windows executable parsing)
- pyelftools (Linux ELF parsing)
- pdfminer.six (PDF extraction)
- python-docx (Word document parsing)
- BeautifulSoup4 (HTML parsing)

---

# 📦 Technologies / Libraries / Tools

| Tool | Purpose |
|------|--------|
| PySide6 | GUI Framework |
| PEfile | PE file parsing |
| pyelftools | ELF file parsing |
| pdfminer.six | PDF text extraction |
| python-docx | DOCX parsing |
| BeautifulSoup | HTML parsing |
| Python standard libraries | Core logic |

---

# 📁 GUI / Project Structure

```

universal_analyzer_v4/
│
├── main.py
├── gui.py
├── detector.py
├── entropy.py
├── exporter.py
├── utils.py
│
├── parsers/
│   ├── pe.py
│   ├── elf.py
│   ├── docx_parser.py
│   ├── pdf_parser.py
│   ├── html_parser.py
│   ├── text_parser.py

````

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/syedshaheerhussain/universal-file-analyzer.git
cd universal-file-analyzer
````

---

## 2. Install Dependencies

```bash
pip install pyside6 pefile pyelftools python-docx pdfminer.six beautifulsoup4
```

---

## 3. Run Application

```bash
python main.py
```

---

# ▶️ How to Run

1. Open terminal / command prompt
2. Navigate to project folder
3. Run:

```bash
python main.py
```

4. GUI will open
5. Click **Open File**
6. Select any file (EXE, PDF, DOCX, TXT, HTML, ELF)

---

# 🧪 Features

## 🔹 File Support

* `.exe`
* `.dll`
* `.elf`
* `.pdf`
* `.docx`
* `.txt`
* `.html`
* `.xlsx`

---

## 🔹 Analysis Features

* PE Structure Analysis
* ELF Structure Analysis
* Imports & Exports Viewer
* Sections Viewer
* Strings Extraction
* Hex Viewer
* Document Parsing
* Entropy Analysis (Malware Detection)

---

## 🔹 GUI Features

* Modern Dark UI
* Tab-based layout
* Search system
* Export functionality
* Tree-based structure view
* Responsive interface

---

## 🔹 Security / Forensics Features

* File entropy detection
* Packed file detection (high entropy)
* Suspicious binary identification
* Deep file inspection

---

# ⚙️ Functions / How It Works

## 1. File Detection

Automatically detects file type using extension.

## 2. Parsing Engine

Each file type is routed to a dedicated parser:

* PE → pefile
* ELF → pyelftools
* DOCX → python-docx
* PDF → pdfminer
* HTML → BeautifulSoup

---

## 3. Structure Builder

Creates hierarchical tree view:

* Sections
* Imports
* Exports
* Document paragraphs
* Tables

---

## 4. Strings Extraction

Scans binary data and extracts readable text.

---

## 5. Hex Viewer

Displays raw binary in hexadecimal format.

---

## 6. Entropy Analyzer

Calculates randomness of file:

* Low → Normal file
* Medium → Suspicious
* High → Packed / Malware-like

---

## 7. Export System

Exports analysis into JSON format.

---

## 8. Search Engine

Search inside:

* Strings
* Hex
* Info panel

---

# 📊 Working Code Example

```python
from entropy import entropy

data = open("sample.exe", "rb").read()
print(entropy(data))
```

---

# 🧪 Example Use Case

### Malware Analysis

1. Load suspicious `.exe`
2. Check entropy (high = packed)
3. Inspect imports (suspicious API calls)
4. Extract strings (URLs, commands)
5. Analyze structure

---

### Document Forensics

1. Load PDF or DOCX
2. Extract hidden text
3. Analyze metadata
4. Search keywords

---

# 📌 Objectives Achieved

✔ Multi-file analyzer
✔ Reverse engineering support
✔ Malware detection via entropy
✔ GUI-based inspection tool
✔ Cross-format file support
✔ Export system
✔ Search engine

---

# 👨‍💻 Learning Outcomes / What I Learned

* File structure analysis (PE & ELF)
* GUI development using PySide6
* Binary data processing
* Malware detection basics
* File parsing techniques
* Software architecture design
* Modular programming

---

# 📢 Target Audience

* Cybersecurity students
* Reverse engineering learners
* Malware analysts
* Software developers
* Ethical hackers
* Researchers

---

# 🚀 Future Enhancements

* Disassembler integration (Capstone)
* Function call graph
* Live memory analysis
* Malware sandbox
* Plugin system (IDA-style)
* Advanced UI dashboards
* Real-time file monitoring

---

# ⚠️ Important Notes / Disclaimer

* This tool is for **educational purposes only**
* Do NOT use on unauthorized systems
* Some binaries may not parse fully (packed files)
* Large files may take time to analyze

---

# 🧯 Cautions

* Do not run unknown executables outside sandbox
* High entropy files may be malware
* Always verify file sources

---

# 💻 Implementation & Value

This project demonstrates:

* Advanced Python programming
* GUI application development
* Cybersecurity fundamentals
* Reverse engineering concepts
* Real-world forensic tool design

---

# 📌 Support & Engagement

If you like this project:

⭐ Star this repository
🔁 Share with others
👤 Follow developer:
👉 [https://github.com/syedshaheerhussain](https://github.com/syedshaheerhussain)

---

# 🧠 License

This project is open-source for educational use.
You may modify and improve it for learning purposes.

---

# 🏁 Final Words

This project is a **mini reverse engineering + forensic suite** built for learning and research purposes.
It can be expanded into a professional-grade security tool with advanced features.

---
