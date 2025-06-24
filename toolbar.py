from PyQt5.QtWidgets import QToolBar, QAction

def create_toolbar(parent):
    toolbar = QToolBar("Main Toolbar")
    parent.addToolBar(toolbar)

    def add_action(name, callback):
        action = QAction(name, parent)
        action.triggered.connect(callback)
        toolbar.addAction(action)
        return action

    add_action("New", parent.new_file)
    add_action("Open", parent.open_file)
    add_action("Save", parent.save_file)
    toolbar.addSeparator()
    add_action("Cut", parent.cut_text)
    add_action("Copy", parent.copy_text)
    add_action("Paste", parent.paste_text)
    toolbar.addSeparator()
    add_action("Find", parent.show_find_dialog)
    add_action("Toggle Theme", parent.toggle_theme)