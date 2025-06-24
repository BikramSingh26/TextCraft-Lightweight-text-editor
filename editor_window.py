from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QStatusBar,
                            QTabWidget, QMessageBox, QFileDialog, QSplitter)
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.Qsci import QsciScintilla
from editor_tab import create_editor_tab
from toolbar import create_toolbar
from menus import create_menus
from theme import set_theme_on_editor, apply_theme_to_all_tabs
import os
from terminal_widget import TerminalWidget

class ModernTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Text Editor")
        self.setGeometry(100, 100, 800, 600)
        self.current_file = None
        self.unsaved_changes = False
        self.autosave_interval = 30000  # 30 seconds
        self.current_theme = 'dark'

        self.create_ui()

        self.autosave_timer = QTimer(self)
        self.autosave_timer.timeout.connect(self.autosave)
        self.autosave_timer.start(self.autosave_interval)

        apply_theme_to_all_tabs(self, self.current_theme)

    def create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        splitter = QSplitter()
        splitter.setOrientation(Qt.Vertical)

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        splitter.addWidget(self.tab_widget)

        # Add terminal widget at the bottom
        self.terminal_widget = TerminalWidget(self)
        splitter.addWidget(self.terminal_widget)
        splitter.setSizes([500, 150])  # Initial sizes

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(splitter)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.update_status_bar()

        self.new_file()
        create_toolbar(self)
        create_menus(self)

    def add_new_tab(self, filename="Untitled", content=""):
        editor = create_editor_tab()
        if content:
            editor.setText(content)
        self.tab_widget.addTab(editor, filename)
        self.tab_widget.setCurrentIndex(self.tab_widget.count() - 1)
        set_theme_on_editor(editor, self.current_theme)
        return editor

    def current_editor(self):
        return self.tab_widget.currentWidget()

    # File Operations
    def new_file(self):
        """Create a new empty tab"""
        self.add_new_tab()
        self.current_file = None
        self.unsaved_changes = False
        self.update_status_bar()

    def open_file(self):
        """Open a file in a new tab"""
        filename, _ = QFileDialog.getOpenFileName(self, "Open File")
        if filename:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                self.add_new_tab(os.path.basename(filename), content)
                self.current_file = filename
                self.unsaved_changes = False
                self.update_status_bar()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not open file:\n{str(e)}")

    def save_file(self):
        """Save the current file"""
        if self.current_file:
            try:
                # Ensure directory exists
                os.makedirs(os.path.dirname(self.current_file), exist_ok=True)
                with open(self.current_file, 'w') as file:
                    file.write(self.current_editor().text())
                self.unsaved_changes = False
                self.update_status_bar()
                return True
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not save file:\n{str(e)}")
                return False
        else:
            return self.save_file_as()

    def save_file_as(self):
        """Save the current file with a new name"""
        filename, _ = QFileDialog.getSaveFileName(self, "Save File")
        if filename:
            try:
                # Ensure directory exists
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, 'w') as file:
                    file.write(self.current_editor().text())
                self.current_file = filename
                self.unsaved_changes = False
                self.tab_widget.setTabText(self.tab_widget.currentIndex(), os.path.basename(filename))
                self.update_status_bar()
                return True
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not save file:\n{str(e)}")
                return False
        return False

    # Tab Management
    def close_tab(self, index):
        widget = self.tab_widget.widget(index)
        
        if self.has_unsaved_changes(widget):
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "You have unsaved changes. Save before closing?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Save:
                if not self.save_file():
                    return  # User cancelled save
            elif reply == QMessageBox.Cancel:
                return  # Don't close the tab
        
        self.tab_widget.removeTab(index)
        
        if self.tab_widget.count() == 0:
            self.new_file()

    def has_unsaved_changes(self, editor=None):
        """Check if there are unsaved changes"""
        editor = editor or self.current_editor()
        # Basic implementation - you might want to track changes per tab
        return self.unsaved_changes

    # Text Operations
    def cut_text(self):
        editor = self.current_editor()
        if editor:
            editor.cut()

    def copy_text(self):
        editor = self.current_editor()
        if editor:
            editor.copy()

    def paste_text(self):
        editor = self.current_editor()
        if editor:
            editor.paste()

    def undo(self):
        editor = self.current_editor()
        if editor:
            editor.undo()

    def redo(self):
        editor = self.current_editor()
        if editor:
            editor.redo()

    # Find/Replace
    def show_find_dialog(self):
        from find_replace import show_find_dialog
        show_find_dialog(self)

    # Zoom Operations
    def zoom_in(self):
        editor = self.current_editor()
        if editor:
            editor.zoomIn()

    def zoom_out(self):
        editor = self.current_editor()
        if editor:
            editor.zoomOut()

    # Theme Operations
    def toggle_theme(self):
        from theme import toggle_theme
        current = self.current_editor().paper().name()
        self.current_theme = 'light' if current == "#2b2b2b" else 'dark'
        toggle_theme(self)

    # Status and Autosave
    def update_status_bar(self):
        """Update the status bar with current file info"""
        if self.current_file:
            self.status_bar.showMessage(f"File: {self.current_file} | {'Unsaved changes' if self.unsaved_changes else 'Saved'}")
        else:
            self.status_bar.showMessage("New file | Unsaved changes")

    def autosave(self):
        """Autosave functionality"""
        if self.unsaved_changes and self.current_file:
            self.save_file()