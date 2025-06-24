from PyQt5.QtWidgets import QAction

def create_menus(parent):
    menubar = parent.menuBar()

    # File Menu
    file_menu = menubar.addMenu("File")
    file_menu.addAction(QAction("New", parent, triggered=parent.new_file))
    file_menu.addAction(QAction("Open...", parent, triggered=parent.open_file))
    file_menu.addAction(QAction("Save", parent, triggered=parent.save_file))
    file_menu.addAction(QAction("Save As...", parent, triggered=parent.save_file_as))
    file_menu.addSeparator()
    file_menu.addAction(QAction("Exit", parent, triggered=parent.close))

    # Edit Menu
    edit_menu = menubar.addMenu("Edit")
    edit_menu.addAction(QAction("Undo", parent, triggered=parent.undo))
    edit_menu.addAction(QAction("Redo", parent, triggered=parent.redo))
    edit_menu.addSeparator()
    edit_menu.addAction(QAction("Cut", parent, triggered=parent.cut_text))
    edit_menu.addAction(QAction("Copy", parent, triggered=parent.copy_text))
    edit_menu.addAction(QAction("Paste", parent, triggered=parent.paste_text))
    edit_menu.addSeparator()
    edit_menu.addAction(QAction("Find...", parent, triggered=parent.show_find_dialog))

    # View Menu
    view_menu = menubar.addMenu("View")
    view_menu.addAction(QAction("Zoom In", parent, triggered=parent.zoom_in))
    view_menu.addAction(QAction("Zoom Out", parent, triggered=parent.zoom_out))
    view_menu.addSeparator()
    view_menu.addAction(QAction("Toggle Theme", parent, triggered=parent.toggle_theme))