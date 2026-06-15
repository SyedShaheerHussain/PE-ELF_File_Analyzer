from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QTextEdit, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QLineEdit, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt

from detector import detect_file_type
from utils import extract_strings, to_hex
from entropy import entropy, entropy_label
from exporter import export_json

from parsers.pe import parse_pe
from parsers.elf import parse_elf
from parsers.docx_parser import parse_docx
from parsers.pdf_parser import parse_pdf
from parsers.html_parser import parse_html
from parsers.text_parser import parse_text


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Universal Analyzer v4 PRO")
        self.resize(1400, 850)

        # 🔥 CLEAN DARK THEME (HIGH CONTRAST)
        self.setStyleSheet("""
            QWidget {
                background-color: #0b0f19;
                color: #e6e6e6;
                font-size: 13px;
            }

            QPushButton {
                background-color: #1f2a44;
                color: white;
                padding: 8px;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #2c3e66;
            }

            QTextEdit, QTreeWidget, QLineEdit {
                background-color: #111827;
                color: #ffffff;
                border: 1px solid #2b3446;
            }

            QTabWidget::pane {
                border: 1px solid #2b3446;
            }

            QTabBar::tab {
                background: #1a2234;
                padding: 8px;
                margin: 2px;
            }

            QTabBar::tab:selected {
                background: #2c3e66;
            }
        """)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # ================= TOP BUTTONS =================
        top_bar = QHBoxLayout()

        self.btn_open = QPushButton("📂 Open File")
        self.btn_open.clicked.connect(self.open_file)

        self.btn_export = QPushButton("💾 Export JSON")
        self.btn_export.clicked.connect(self.export)

        top_bar.addWidget(self.btn_open)
        top_bar.addWidget(self.btn_export)

        # ================= SEARCH BOX =================
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("🔍 Search in results...")
        self.search_box.textChanged.connect(self.search_text)

        # ================= TABS =================
        self.tabs = QTabWidget()

        self.info = QTextEdit()
        self.hex = QTextEdit()
        self.strings = QTextEdit()

        self.structure = QTreeWidget()
        self.structure.setHeaderLabels(["Item", "Value"])

        self.search_tab = QTextEdit()

        self.tabs.addTab(self.info, "📊 Info")
        self.tabs.addTab(self.structure, "🌳 Structure")
        self.tabs.addTab(self.strings, "🔤 Strings")
        self.tabs.addTab(self.hex, "🧱 Hex")
        self.tabs.addTab(self.search_tab, "🔎 Search Results")

        # ================= ADD UI =================
        main_layout.addLayout(top_bar)
        main_layout.addWidget(self.search_box)
        main_layout.addWidget(self.tabs)

        self.current_data = {}

    # ================= FILE OPEN =================
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self)
        if not path:
            return

        file_type = detect_file_type(path)

        with open(path, "rb") as f:
            raw = f.read()

        # basic views
        self.hex.setText(to_hex(raw))
        self.strings.setText(extract_strings(raw))
        self.structure.clear()

        e = entropy(raw)

        self.info.setText(
            f"📁 File: {path}\n"
            f"📦 Type: {file_type}\n"
            f"📊 Entropy: {e:.2f} ({entropy_label(e)})"
        )

        # ================= PE =================
        if file_type == "pe":
            d = parse_pe(path)

            sec = QTreeWidgetItem(["SECTIONS", ""])
            for s in d["sections"]:
                QTreeWidgetItem(sec, [s["name"], s["vaddr"]])
            self.structure.addTopLevelItem(sec)

            imp = QTreeWidgetItem(["IMPORTS", ""])
            for dll, funcs in d["imports"].items():
                dll_item = QTreeWidgetItem(imp, [dll, ""])
                for f in funcs:
                    QTreeWidgetItem(dll_item, [f, ""])
            self.structure.addTopLevelItem(imp)

            exp = QTreeWidgetItem(["EXPORTS", ""])
            for e in d["exports"]:
                QTreeWidgetItem(exp, [e, ""])
            self.structure.addTopLevelItem(exp)

        # ================= ELF =================
        elif file_type == "elf":
            d = parse_elf(path)
            sec = QTreeWidgetItem(["SECTIONS", ""])
            for s in d["sections"]:
                QTreeWidgetItem(sec, [s["name"], s["addr"]])
            self.structure.addTopLevelItem(sec)

        # ================= DOCS =================
        elif file_type == "docx":
            d = parse_docx(path)
            para = QTreeWidgetItem(["PARAGRAPHS", ""])
            for p in d["paragraphs"]:
                QTreeWidgetItem(para, [p[:80], ""])
            self.structure.addTopLevelItem(para)

        elif file_type == "html":
            d = parse_html(path)
            root = QTreeWidgetItem(["TITLE", d["title"]])
            self.structure.addTopLevelItem(root)

        elif file_type == "text":
            d = parse_text(path)
            self.info.setText(d["text"])

        # save for export
        self.current_data = {
            "info": self.info.toPlainText(),
            "strings": self.strings.toPlainText()
        }

    # ================= SEARCH =================
    def search_text(self):
        key = self.search_box.text().lower()

        all_text = (
            self.info.toPlainText()
            + self.strings.toPlainText()
            + self.hex.toPlainText()
        )

        results = [
            line for line in all_text.splitlines()
            if key in line.lower()
        ]

        self.search_tab.setText("\n".join(results[:300]))

    # ================= EXPORT =================
    def export(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save JSON", "", "JSON (*.json)")
        if path:
            export_json(path, self.current_data)