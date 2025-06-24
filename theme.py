from PyQt5.QtGui import QColor

def set_theme_on_editor(editor, theme):
    if editor:
        lexer = editor.lexer()
        if theme == 'dark':
            editor.setPaper(QColor("#2b2b2b"))
            editor.setColor(QColor("#a9b7c6"))
            editor.setMarginsBackgroundColor(QColor("#333333"))
            editor.setMarginsForegroundColor(QColor("#ffffff"))
            if lexer:
                lexer.setDefaultPaper(QColor("#2b2b2b"))
                lexer.setDefaultColor(QColor("#a9b7c6"))
                lexer.setColor(QColor("#cc7832"), 1)  # Keywords
                lexer.setColor(QColor("#6a8759"), 2)  # Strings
                lexer.setColor(QColor("#bbb529"), 3)  # Comments
                lexer.setColor(QColor("#9876aa"), 4)  # Numbers
        else:
            editor.setPaper(QColor("#ffffff"))
            editor.setColor(QColor("#000000"))
            editor.setMarginsBackgroundColor(QColor("#e0e0e0"))
            editor.setMarginsForegroundColor(QColor("#333333"))
            if lexer:
                lexer.setDefaultPaper(QColor("#ffffff"))
                lexer.setDefaultColor(QColor("#000000"))
                lexer.setColor(QColor("#0000ff"), 1)  # Keywords
                lexer.setColor(QColor("#008000"), 2)  # Strings
                lexer.setColor(QColor("#ff00ff"), 3)  # Comments
                lexer.setColor(QColor("#808080"), 4)  # Numbers

def apply_theme_to_all_tabs(parent, theme):
    for i in range(parent.tab_widget.count()):
        editor = parent.tab_widget.widget(i)
        set_theme_on_editor(editor, theme)

def toggle_theme(parent):
    current = parent.current_editor().paper().name()
    new_theme = 'light' if current == "#2b2b2b" else 'dark'
    apply_theme_to_all_tabs(parent, new_theme)