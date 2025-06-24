import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from editor_window import ModernTextEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont("Consolas", 11))

    editor = ModernTextEditor()
    editor.show()
    sys.exit(app.exec_())