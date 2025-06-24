from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
import subprocess

class TerminalWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(8, 8, 8, 8)
        self.layout.setSpacing(6)

        self.output = QPlainTextEdit(self)
        self.output.setReadOnly(True)
        self.output.setStyleSheet('''
            QPlainTextEdit {
                background: #23272e;
                color: #d4d4d4;
                font-family: Consolas, monospace;
                border-radius: 8px;
                padding: 8px;
                border: 1px solid #444;
            }
        ''')
        self.layout.addWidget(self.output)

        # Input and clear button in a horizontal layout
        input_layout = QHBoxLayout()
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Enter command and press Enter...")
        self.input.returnPressed.connect(self.run_command)
        self.input.setStyleSheet('''
            QLineEdit {
                background: #181c20;
                color: #e0e0e0;
                border-radius: 6px;
                padding: 6px 10px;
                border: 1.5px solid #555;
                font-family: Consolas, monospace;
            }
            QLineEdit:focus {
                border: 1.5px solid #0078d7;
            }
        ''')
        input_layout.addWidget(self.input)

        self.clear_btn = QPushButton("Clear", self)
        self.clear_btn.setCursor(Qt.PointingHandCursor)
        self.clear_btn.setStyleSheet('''
            QPushButton {
                background: #2d323b;
                color: #b0b0b0;
                border-radius: 6px;
                padding: 6px 16px;
                border: 1px solid #444;
            }
            QPushButton:hover {
                background: #3a3f4b;
                color: #fff;
            }
        ''')
        self.clear_btn.clicked.connect(self.output.clear)
        input_layout.addWidget(self.clear_btn)

        self.layout.addLayout(input_layout)
        self.setMinimumHeight(150)
        self.setStyleSheet('''
            QWidget {
                background: #181c20;
                border-radius: 8px;
            }
        ''')

    def run_command(self):
        cmd = self.input.text().strip()
        if not cmd:
            return
        self.output.appendPlainText(f"> {cmd}")
        try:
            # Use shell=True for Windows compatibility
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            if stdout:
                self.output.appendPlainText(stdout)
            if stderr:
                self.output.appendPlainText(stderr)
        except Exception as e:
            self.output.appendPlainText(f"Error: {e}")
        self.input.clear() 