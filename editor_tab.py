from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5.QtGui import QColor, QFont

def create_editor_tab():
    editor = QsciScintilla()
    editor.setMarginType(0, QsciScintilla.NumberMargin)
    editor.setMarginWidth(0, "000")
    editor.setMarginsBackgroundColor(QColor("#333333"))
    editor.setMarginsForegroundColor(QColor("#ffffff"))

    lexer = QsciLexerPython()
    lexer.setDefaultFont(QFont("Consolas", 11))
    editor.setLexer(lexer)

    settings = get_editor_settings()
    for setting, value in settings.items():
        getattr(editor, setting)(value)

    return editor

def get_editor_settings():
    return {
        "setBraceMatching": QsciScintilla.SloppyBraceMatch,
        "setIndentationGuides": True,
        "setAutoIndent": True,
        "setTabWidth": 4,
        "setIndentationsUseTabs": False,
        "setUtf8": True,
    }