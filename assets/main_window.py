import json
import os
import re
import logging
from datetime import datetime
from typing import Optional
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .models import Schema, VariableType
from .design_system import StyleSheets
from .widgets import Card
from .dialogs import VariableDialog
from .schema_manager import SchemaManager
from templates.preview_dialog import TemplatePreviewDialog

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Main application window"""

    # Font and size parameters for easy adjustment
    main_font_family = "Consolas, Monaco, JetBrains Mono, monospace"
    main_font_size = 20
    header_font_size = 24
    preview_font_family = "Consolas"
    preview_font_size = 18

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schema Designer Pro")
        self.setGeometry(100, 100, 1800, 1000)  # Larger default size

        # Initialize dark mode state
        self.dark_mode = False

        # Apply styles
        self.setStyleSheet(StyleSheets.get_application_style(dark_mode=self.dark_mode))

        # Initialize components
        self.schema_manager = SchemaManager()
        self.current_schema: Optional[Schema] = None
        self.unsaved_changes = False

        # Setup UI
        self._setup_ui()
        self._setup_shortcuts()
        self._setup_auto_save()

        # Show welcome message
        self._show_status("Welcome to Schema Designer Pro", "info")

    def _setup_ui(self):
        """Setup the main UI"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_v_layout = QVBoxLayout(central_widget)
        main_v_layout.setSpacing(0)
        main_v_layout.setContentsMargins(0, 0, 0, 0)

        # ASCII Art Header
        header_widget = self._create_ascii_header()
        main_v_layout.addWidget(header_widget)

        # Content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setSpacing(24)
        content_layout.setContentsMargins(24, 24, 24, 24)

        # Create panels
        left_panel = self._create_schema_panel()
        center_panel = self._create_editor_panel()
        right_panel = self._create_preview_panel()

        # Add to splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([450, 800, 550])

        content_layout.addWidget(splitter)
        main_v_layout.addWidget(content_widget, 1)

        # Status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

        # Add dark mode toggle to status bar
        self.dark_mode_btn = QToolButton()
        self.dark_mode_btn.setObjectName("darkModeToggle")
        self.dark_mode_btn.setText("◐")
        self.dark_mode_btn.setToolTip("Toggle Dark Mode")
        self.dark_mode_btn.clicked.connect(self._toggle_dark_mode)
        self.status_bar.addPermanentWidget(self.dark_mode_btn)

    def _create_ascii_header(self) -> QWidget:
        """Create ASCII art header with instructions"""
        header = QWidget()
        header.setStyleSheet(
            """
            QWidget {
                background-color: #000000;
                border-bottom: 3px solid #000000;
            }
        """
        )
        header.setFixedHeight(140)

        layout = QVBoxLayout(header)
        layout.setContentsMargins(24, 16, 24, 16)

        # ASCII Art
        ascii_art = QLabel()
        ascii_art.setStyleSheet(
            f"""
            QLabel {{
                color: #FFFFFF;
                font-family: {self.main_font_family};
                font-size: {self.header_font_size}px;
                line-height: 1.2;
                font-weight: 400;
            }}
            """
        )

        ascii_text = """╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗
║  ┌─────────┐     ┌─────────────┐     ┌──────────┐        SCHEMA DESIGNER PRO                     ║
║  │ SCHEMAS ├─────┤ TRANSFORMER ├─────┤   JSON   │        数据模式设计专业版                        ║
║  └─────────┘     └─────────────┘     └──────────┘                                                ║
║                                                           Design → Transform → Export               ║
║  [Ctrl+N] New Schema  [Ctrl+T] Template  [Ctrl+S] Save   设计 → 转换 → 导出                        ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝"""

        ascii_art.setText(ascii_text)
        ascii_art.setAlignment(Qt.AlignLeft)
        layout.addWidget(ascii_art)

        return header

    def _toggle_dark_mode(self):
        """Toggle between light and dark mode"""
        self.dark_mode = not self.dark_mode

        # Update icon
        self.dark_mode_btn.setText("☀️" if self.dark_mode else "🌙")
        self.dark_mode_btn.setToolTip(
            "Switch to Light Mode" if self.dark_mode else "Switch to Dark Mode"
        )

        # Apply new stylesheet
        self.setStyleSheet(StyleSheets.get_application_style(dark_mode=self.dark_mode))

        # Show status
        mode = "Dark" if self.dark_mode else "Light"
        self._show_status(f"Switched to {mode} Mode")

    def _create_schema_panel(self) -> QWidget:
        """Create the schema list panel"""
        panel = Card()
        layout = QVBoxLayout(panel)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Schemas")
        title.setObjectName("heading2")
        header_layout.addWidget(title)

        # New schema button
        new_btn = QToolButton()
        new_btn.setText("＋")
        new_btn.setToolTip("Create new schema")
        new_btn.setStyleSheet(
            """
            QToolButton {
                font-size: 30px;
                font-weight: 300;
            }
        """
        )
        new_btn.clicked.connect(self._create_schema)
        header_layout.addWidget(new_btn)

        # Template button
        template_btn = QToolButton()
        template_btn.setText("⊞")
        template_btn.setToolTip("Create from template")
        template_btn.setStyleSheet(
            """
            QToolButton {
                font-size: 30px;
                font-weight: 300;
            }
        """
        )
        template_btn.clicked.connect(self._create_from_template)
        header_layout.addWidget(template_btn)

        layout.addLayout(header_layout)

        # Search
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search schemas...")
        search_input.textChanged.connect(self._filter_schemas)
        layout.addWidget(search_input)

        # Schema list
        self.schema_list = QListWidget()
        self.schema_list.setAlternatingRowColors(True)
        self.schema_list.itemClicked.connect(self._load_schema)
        self.schema_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.schema_list.customContextMenuRequested.connect(self._show_schema_menu)
        layout.addWidget(self.schema_list, 1)

        # Action buttons
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(8)

        # Template button (Alternative placement as full button)
        template_full_btn = QPushButton("CREATE FROM TEMPLATE")
        template_full_btn.setObjectName("secondary")
        template_full_btn.clicked.connect(self._create_from_template)
        btn_layout.addWidget(template_full_btn)

        duplicate_btn = QPushButton("DUPLICATE")
        duplicate_btn.setObjectName("secondary")
        duplicate_btn.clicked.connect(self._duplicate_schema)

        delete_btn = QPushButton("DELETE")
        delete_btn.setObjectName("danger")
        delete_btn.clicked.connect(self._delete_schema)

        btn_layout.addWidget(duplicate_btn)
        btn_layout.addWidget(delete_btn)
        layout.addLayout(btn_layout)

        # File operations
        layout.addWidget(self._create_separator())

        file_label = QLabel("File Operations")
        file_label.setObjectName("heading3")
        layout.addWidget(file_label)

        file_btn_layout = QVBoxLayout()
        file_btn_layout.setSpacing(8)

        import_btn = QPushButton("IMPORT JSON")
        import_btn.setObjectName("secondary")
        import_btn.clicked.connect(self._import_json)

        export_btn = QPushButton("EXPORT ALL")
        export_btn.clicked.connect(self._export_json)

        export_selected_btn = QPushButton("EXPORT SELECTED")
        export_selected_btn.setObjectName("secondary")
        export_selected_btn.clicked.connect(self._export_selected)

        file_btn_layout.addWidget(import_btn)
        file_btn_layout.addWidget(export_btn)
        file_btn_layout.addWidget(export_selected_btn)
        layout.addLayout(file_btn_layout)

        return panel

    def _create_editor_panel(self) -> QWidget:
        """Create the schema editor panel"""
        panel = Card()
        layout = QVBoxLayout(panel)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Schema Editor")
        title.setObjectName("heading2")
        header_layout.addWidget(title)

        # Save indicator
        self.save_indicator = QLabel("●")
        self.save_indicator.setStyleSheet(
            """
            QLabel {
                color: #059669;
                font-size: 20px;
            }
        """
        )
        self.save_indicator.setToolTip("All changes saved")
        header_layout.addWidget(self.save_indicator)
        header_layout.addStretch()

        layout.addLayout(header_layout)

        # Tabs
        self.editor_tabs = QTabWidget()
        self.editor_tabs.setDocumentMode(True)

        # Basic info tab
        basic_tab = self._create_basic_tab()
        self.editor_tabs.addTab(basic_tab, "Basic Information")

        # Variables tab
        variables_tab = self._create_variables_tab()
        self.editor_tabs.addTab(variables_tab, "Variables")

        layout.addWidget(self.editor_tabs, 1)

        # Save button
        save_btn = QPushButton("SAVE SCHEMA")
        save_btn.clicked.connect(self._save_schema)
        layout.addWidget(save_btn)

        return panel

    def _create_basic_tab(self) -> QWidget:
        """Create the basic information tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameStyle(QFrame.NoFrame)

        scroll_widget = QWidget()
        form_layout = QFormLayout(scroll_widget)
        form_layout.setSpacing(24)
        form_layout.setLabelAlignment(Qt.AlignRight)

        # Schema name
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Unique schema identifier")
        self.name_input.textChanged.connect(self._mark_unsaved)
        form_layout.addRow("Schema Name *", self.name_input)

        # Page titles
        self.title_cn_input = QLineEdit()
        self.title_cn_input.setPlaceholderText("中文页面标题")
        self.title_cn_input.textChanged.connect(self._mark_unsaved)
        form_layout.addRow("Page Title (CN)", self.title_cn_input)

        self.title_en_input = QLineEdit()
        self.title_en_input.setPlaceholderText("English page title")
        self.title_en_input.textChanged.connect(self._mark_unsaved)
        form_layout.addRow("Page Title (EN)", self.title_en_input)

        # Options
        form_layout.addRow(self._create_separator())

        options_label = QLabel("Options")
        options_label.setObjectName("heading3")
        form_layout.addRow(options_label)

        self.match_img_combo = QComboBox()
        self.match_img_combo.addItems(["yes", "no"])
        self.match_img_combo.setCurrentText("no")
        self.match_img_combo.currentTextChanged.connect(self._mark_unsaved)
        form_layout.addRow("Match Image", self.match_img_combo)

        self.filter_with_combo = QComboBox()
        self.filter_with_combo.addItems(["yes", "no"])
        self.filter_with_combo.setCurrentText("no")
        self.filter_with_combo.currentTextChanged.connect(self._mark_unsaved)
        form_layout.addRow("Filter With", self.filter_with_combo)

        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)

        return tab

    def _create_variables_tab(self) -> QWidget:
        """Create the variables tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(16)

        # Variable type selector
        type_layout = QHBoxLayout()

        self.var_type_combo = QComboBox()
        self.var_type_combo.addItems(
            [
                "Basic Variable",
                "More Variable",
                "Image Variable",
                "URL Variable",
                "Array Variable",
                "Language Item Variable",
            ]
        )
        type_layout.addWidget(QLabel("Type:"))
        type_layout.addWidget(self.var_type_combo, 1)

        add_var_btn = QPushButton("ADD VARIABLE")
        add_var_btn.clicked.connect(self._add_variable)
        type_layout.addWidget(add_var_btn)

        layout.addLayout(type_layout)

        # Variables list
        self.variables_list = QListWidget()
        self.variables_list.setAlternatingRowColors(True)
        self.variables_list.itemDoubleClicked.connect(self._edit_variable)
        self.variables_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.variables_list.customContextMenuRequested.connect(self._show_variable_menu)
        layout.addWidget(self.variables_list, 1)

        # Variable actions
        var_btn_layout = QHBoxLayout()

        edit_btn = QPushButton("EDIT")
        edit_btn.setObjectName("secondary")
        edit_btn.clicked.connect(self._edit_variable)

        delete_btn = QPushButton("DELETE")
        delete_btn.setObjectName("danger")
        delete_btn.clicked.connect(self._delete_variable)

        var_btn_layout.addWidget(edit_btn)
        var_btn_layout.addWidget(delete_btn)
        var_btn_layout.addStretch()

        layout.addLayout(var_btn_layout)

        return tab

    def _create_preview_panel(self) -> QWidget:
        """Create the JSON preview panel"""
        panel = Card()
        layout = QVBoxLayout(panel)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel("JSON Preview")
        title.setObjectName("heading2")
        title.setStyleSheet(
            f"font-family: {self.main_font_family}; font-size: {self.header_font_size}px; font-weight: 600;"
        )
        header_layout.addWidget(title)

        # Format button
        format_btn = QToolButton()
        format_btn.setText("{ }")
        format_btn.setToolTip("Format JSON")
        format_btn.clicked.connect(self._format_json)
        header_layout.addWidget(format_btn)

        # Copy button
        copy_btn = QToolButton()
        copy_btn.setText("⎘")
        copy_btn.setToolTip("Copy to clipboard")
        copy_btn.clicked.connect(self._copy_json)
        header_layout.addWidget(copy_btn)

        header_layout.addStretch()
        layout.addLayout(header_layout)

        # Preview text
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setFont(QFont(self.preview_font_family, self.preview_font_size))
        layout.addWidget(self.preview_text, 1)

        return panel

    def _create_separator(self) -> QFrame:
        """Create a horizontal separator"""
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet(
            """
            QFrame {
                background-color: #E5E7EB;
                max-height: 2px;
                margin: 20px 0;
            }
        """
        )
        return separator

    def _setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        shortcuts = [
            ("Ctrl+N", self._create_schema),
            ("Ctrl+T", self._create_from_template),
            ("Ctrl+S", self._save_schema),
            ("Ctrl+O", self._import_json),
            ("Ctrl+E", self._export_json),
            ("Delete", self._delete_schema),
            ("F2", self._edit_variable),
            ("Ctrl+D", self._toggle_dark_mode),  # Added dark mode shortcut
        ]

        for key, func in shortcuts:
            QShortcut(QKeySequence(key), self, func)

    def _setup_auto_save(self):
        """Setup auto-save timer"""
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self._auto_save)
        self.auto_save_timer.start(60000)  # Auto-save every minute

    def _mark_unsaved(self):
        """Mark that there are unsaved changes"""
        self.unsaved_changes = True
        self.save_indicator.setStyleSheet(
            """
            QLabel {
                color: #D97706;
                font-size: 20px;
            }
        """
        )
        self.save_indicator.setToolTip("Unsaved changes")

    def _mark_saved(self):
        """Mark that all changes are saved"""
        self.unsaved_changes = False
        self.save_indicator.setStyleSheet(
            """
            QLabel {
                color: #059669;
                font-size: 20px;
            }
        """
        )
        self.save_indicator.setToolTip("All changes saved")

    def _show_status(self, message: str, status_type: str = "info"):
        """Show status message"""
        self.status_bar.showMessage(message, 5000)

    def _update_schema_list(self):
        """Update the schema list widget"""
        self.schema_list.clear()
        for name in sorted(self.schema_manager.schemas.keys()):
            self.schema_list.addItem(name)

    def _update_variables_list(self):
        """Update the variables list widget"""
        self.variables_list.clear()
        if not self.current_schema:
            return

        for var_type in VariableType:
            var_list = getattr(self.current_schema, var_type.value, [])
            for var in var_list:
                type_label = var_type.name.replace("_", " ").title()
                item_text = f"[{type_label}] {var.name}: {var.en_text} / {var.cn_text} (rows: {var.rows})"
                self.variables_list.addItem(item_text)

    def _update_preview(self):
        """Update the JSON preview"""
        try:
            data = self.schema_manager.export_schemas()
            json_str = json.dumps(data, indent=2, ensure_ascii=False)
            self.preview_text.setText(json_str)
        except Exception as e:
            self.preview_text.setText(f"Error: {str(e)}")

    def _clear_editor(self):
        """Clear the editor fields"""
        self.name_input.clear()
        self.title_cn_input.clear()
        self.title_en_input.clear()
        self.match_img_combo.setCurrentText("no")
        self.filter_with_combo.setCurrentText("no")
        self.variables_list.clear()

    def _load_schema_to_editor(self, schema: Schema):
        """Load schema data into editor"""
        self.name_input.setText(schema.name)
        self.title_cn_input.setText(schema.page_title_cn)
        self.title_en_input.setText(schema.page_title_en)
        self.match_img_combo.setCurrentText(schema.match_img)
        self.filter_with_combo.setCurrentText(schema.filter_with)
        self._update_variables_list()
        self._mark_saved()

    # Event handlers
    def _create_schema(self):
        """Create a new schema"""
        name, ok = QInputDialog.getText(
            self,
            "New Schema",
            "Schema name:",
            text=f"schema_{len(self.schema_manager.schemas) + 1}",
        )

        if ok and name:
            if name in self.schema_manager.schemas:
                QMessageBox.warning(self, "Error", "Schema already exists")
                return

            schema = Schema(name=name)
            self.schema_manager.add_schema(schema)
            self.current_schema = schema
            self._update_schema_list()
            self._load_schema_to_editor(schema)
            self._update_preview()
            self._show_status(f"Created new schema: {name}")

    def _create_from_template(self):
        """Create a new schema from template"""
        dialog = TemplatePreviewDialog(self)

        if dialog.exec_() == QDialog.Accepted:
            schema = dialog.get_schema_from_template()
            if schema:
                # Check if schema name already exists
                if schema.name in self.schema_manager.schemas:
                    QMessageBox.warning(
                        self,
                        "Error",
                        f"Schema '{schema.name}' already exists. Please choose a different name.",
                    )
                    return

                # Add the schema
                self.schema_manager.add_schema(schema)
                self.current_schema = schema
                self._update_schema_list()
                self._load_schema_to_editor(schema)
                self._update_preview()
                self._show_status(f"Created schema from template: {schema.name}")

    def _load_schema(self, item):
        """Load selected schema"""
        if self.unsaved_changes:
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "Save current changes?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            )

            if reply == QMessageBox.Save:
                self._save_schema()
            elif reply == QMessageBox.Cancel:
                return

        schema_name = item.text()
        schema = self.schema_manager.get_schema(schema_name)
        if schema:
            self.current_schema = schema
            self._load_schema_to_editor(schema)
            self._show_status(f"Loaded schema: {schema_name}")

    def _save_schema(self):
        """Save current schema"""
        if not self.current_schema:
            self._show_status("No schema to save", "warning")
            return

        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Error", "Schema name is required")
            return

        # Update schema data
        old_name = self.current_schema.name
        self.current_schema.name = name
        self.current_schema.page_title_cn = self.title_cn_input.text()
        self.current_schema.page_title_en = self.title_en_input.text()
        self.current_schema.match_img = self.match_img_combo.currentText()
        self.current_schema.filter_with = self.filter_with_combo.currentText()

        # Update in manager
        if self.schema_manager.update_schema(old_name, self.current_schema):
            self._update_schema_list()
            self._update_preview()
            self._mark_saved()
            self._show_status(f"Saved schema: {name}")
        else:
            QMessageBox.warning(self, "Error", "Schema name already exists")
            self.current_schema.name = old_name

    def _delete_schema(self):
        """Delete selected schema"""
        current = self.schema_list.currentItem()
        if not current:
            return

        schema_name = current.text()
        reply = QMessageBox.question(
            self,
            "Delete Schema",
            f"Delete '{schema_name}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            if self.schema_manager.delete_schema(schema_name):
                self._update_schema_list()
                self._update_preview()
                if self.current_schema and self.current_schema.name == schema_name:
                    self.current_schema = None
                    self._clear_editor()
                self._show_status(f"Deleted schema: {schema_name}")

    def _duplicate_schema(self):
        """Duplicate selected schema"""
        current = self.schema_list.currentItem()
        if not current:
            return

        original_name = current.text()
        new_name, ok = QInputDialog.getText(
            self, "Duplicate Schema", "New schema name:", text=f"{original_name}_copy"
        )

        if ok and new_name:
            if self.schema_manager.duplicate_schema(original_name, new_name):
                self._update_schema_list()
                self._update_preview()
                self._show_status(f"Duplicated: {original_name} → {new_name}")
            else:
                QMessageBox.warning(self, "Error", "Failed to duplicate schema")

    def _add_variable(self):
        """Add a new variable"""
        if not self.current_schema:
            QMessageBox.warning(self, "Error", "No schema selected")
            return

        var_type = self.var_type_combo.currentText()
        dialog = VariableDialog(var_type, parent=self)

        if dialog.exec_() == QDialog.Accepted:
            variable = dialog.get_variable()
            if variable:
                # Map display type to variable type
                type_map = {
                    "Basic Variable": VariableType.BASIC,
                    "More Variable": VariableType.MORE,
                    "Image Variable": VariableType.IMAGE,
                    "URL Variable": VariableType.URL,
                    "Array Variable": VariableType.ARRAY,
                    "Language Item Variable": VariableType.LANGUAGE,
                }

                var_type_enum = type_map.get(var_type)
                if var_type_enum:
                    var_list = getattr(self.current_schema, var_type_enum.value)
                    var_list.append(variable)
                    self._update_variables_list()
                    self._update_preview()
                    self._mark_unsaved()
                    self._show_status(f"Added variable: {variable.name}")

    def _edit_variable(self):
        """Edit selected variable"""
        current = self.variables_list.currentItem()
        if not current or not self.current_schema:
            return

        # Parse variable info from item text
        match = re.match(r"\[([^\]]+)\] ([^:]+):", current.text())
        if not match:
            return

        var_type_str = match.group(1)
        var_name = match.group(2)

        # Find the variable
        variable = None
        var_list = None

        for var_type in VariableType:
            vlist = getattr(self.current_schema, var_type.value)
            for var in vlist:
                if var.name == var_name:
                    variable = var
                    var_list = vlist
                    break
            if variable:
                break

        if variable:
            dialog = VariableDialog(var_type_str, variable, parent=self)
            if dialog.exec_() == QDialog.Accepted:
                new_var = dialog.get_variable()
                if new_var:
                    # Update the variable
                    idx = var_list.index(variable)
                    var_list[idx] = new_var
                    self._update_variables_list()
                    self._update_preview()
                    self._mark_unsaved()
                    self._show_status(f"Updated variable: {new_var.name}")

    def _delete_variable(self):
        """Delete selected variable"""
        current = self.variables_list.currentItem()
        if not current or not self.current_schema:
            return

        # Parse variable info
        match = re.match(r"\[([^\]]+)\] ([^:]+):", current.text())
        if not match:
            return

        var_name = match.group(2)

        reply = QMessageBox.question(
            self,
            "Delete Variable",
            f"Delete variable '{var_name}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            # Find and remove the variable
            for var_type in VariableType:
                var_list = getattr(self.current_schema, var_type.value)
                for var in var_list[:]:
                    if var.name == var_name:
                        var_list.remove(var)
                        self._update_variables_list()
                        self._update_preview()
                        self._mark_unsaved()
                        self._show_status(f"Deleted variable: {var_name}")
                        return

    def _import_json(self):
        """Import schemas from JSON file"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Import JSON", "", "JSON Files (*.json);;All Files (*)"
        )

        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    data = json.load(f)

                self.schema_manager.import_schemas(data)
                self._update_schema_list()
                self._update_preview()
                self._clear_editor()
                self.current_schema = None
                self._show_status(f"Imported {len(data)} schemas")

            except Exception as e:
                QMessageBox.critical(self, "Import Error", str(e))
                logger.error(f"Import error: {e}")

    def _export_json(self):
        """Export all schemas to JSON file"""
        # Create timestamp for filename
        timestamp = datetime.now().strftime("%H_%M_%m_%d_%Y")
        default_filename = f"schemas_{timestamp}.json"

        file_name, _ = QFileDialog.getSaveFileName(
            self, "Export JSON", default_filename, "JSON Files (*.json);;All Files (*)"
        )

        if file_name:
            try:
                data = self.schema_manager.export_schemas()
                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                self._show_status(f"Exported {len(data)} schemas")

            except Exception as e:
                QMessageBox.critical(self, "Export Error", str(e))
                logger.error(f"Export error: {e}")

    def _export_selected(self):
        """Export selected schema"""
        current = self.schema_list.currentItem()
        if not current:
            QMessageBox.warning(self, "Error", "No schema selected")
            return

        schema_name = current.text()
        schema = self.schema_manager.get_schema(schema_name)
        if not schema:
            return

        # Create timestamp for filename
        timestamp = datetime.now().strftime("%H_%M_%m_%d_%Y")
        default_filename = f"{schema_name}_{timestamp}.json"

        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Export Schema",
            default_filename,
            "JSON Files (*.json);;All Files (*)",
        )

        if file_name:
            try:
                data = {schema_name: schema.to_dict()}
                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                self._show_status(f"Exported schema: {schema_name}")

            except Exception as e:
                QMessageBox.critical(self, "Export Error", str(e))
                logger.error(f"Export error: {e}")

    def _format_json(self):
        """Format the JSON preview"""
        try:
            text = self.preview_text.toPlainText()
            if text:
                data = json.loads(text)
                formatted = json.dumps(
                    data, indent=2, ensure_ascii=False, sort_keys=True
                )
                self.preview_text.setText(formatted)
                self._show_status("JSON formatted")
        except Exception as e:
            self._show_status(f"Format error: {str(e)}", "error")

    def _copy_json(self):
        """Copy JSON to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.preview_text.toPlainText())
        self._show_status("Copied to clipboard")

    def _filter_schemas(self, text: str):
        """Filter schema list based on search text"""
        for i in range(self.schema_list.count()):
            item = self.schema_list.item(i)
            item.setHidden(text.lower() not in item.text().lower())

    def _show_schema_menu(self, position):
        """Show context menu for schema list"""
        item = self.schema_list.itemAt(position)
        if not item:
            return

        menu = QMenu(self)
        menu.addAction("Duplicate", self._duplicate_schema)
        menu.addAction("Delete", self._delete_schema)
        menu.addSeparator()
        menu.addAction("Export", self._export_selected)

        menu.exec_(self.schema_list.mapToGlobal(position))

    def _show_variable_menu(self, position):
        """Show context menu for variable list"""
        item = self.variables_list.itemAt(position)
        if not item:
            return

        menu = QMenu(self)
        menu.addAction("Edit", self._edit_variable)
        menu.addAction("Delete", self._delete_variable)

        menu.exec_(self.variables_list.mapToGlobal(position))

    def _auto_save(self):
        """Auto-save current work"""
        if self.unsaved_changes and self.current_schema:
            self._save_schema()

        # Create backup
        if self.schema_manager.schemas:
            try:
                backup_dir = "backups"
                os.makedirs(backup_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = os.path.join(backup_dir, f"backup_{timestamp}.json")

                data = self.schema_manager.export_schemas()
                with open(backup_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                # Keep only last 10 backups
                backups = sorted(
                    [f for f in os.listdir(backup_dir) if f.endswith(".json")]
                )
                if len(backups) > 10:
                    for old_backup in backups[:-10]:
                        os.remove(os.path.join(backup_dir, old_backup))

            except Exception as e:
                logger.error(f"Auto-save error: {e}")

    def closeEvent(self, event):
        """Handle window close event"""
        if self.unsaved_changes:
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "Save changes before closing?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            )

            if reply == QMessageBox.Save:
                self._save_schema()
                event.accept()
            elif reply == QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
