from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

def show_find_dialog(parent):
    dialog = QDialog(parent)
    dialog.setWindowTitle("Find and Replace")
    
    layout = QVBoxLayout()
    find_layout = QHBoxLayout()
    replace_layout = QHBoxLayout()

    find_field = QLineEdit()
    replace_field = QLineEdit()
    find_button = QPushButton("Find")
    replace_button = QPushButton("Replace")

    find_button.clicked.connect(lambda: find_text(parent, find_field.text()))
    replace_button.clicked.connect(lambda: replace_text(parent, find_field.text(), replace_field.text()))

    find_layout.addWidget(find_field)
    find_layout.addWidget(find_button)

    replace_layout.addWidget(replace_field)
    replace_layout.addWidget(replace_button)

    layout.addLayout(find_layout)
    layout.addLayout(replace_layout)

    dialog.setLayout(layout)
    dialog.exec_()

def find_text(parent, text):
    editor = parent.current_editor()
    if editor and text:
        if not editor.findFirst(text, False, False, False, True):
            parent.status_bar.showMessage("Text not found", 2000)

def replace_text(parent, find_text, replace_text):
    editor = parent.current_editor()
    if editor and find_text:
        editor.replace(replace_text)