import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from typing import Optional
from assets.dialogs import ModernDialog
from templates.manager import SchemaTemplate, TemplateManager


class TemplatePreviewDialog(ModernDialog):
    """Dialog for selecting and previewing schema templates"""

    def __init__(self, parent=None):
        super().__init__("Select Schema Template", parent)
        self.template_manager = TemplateManager()
        self.selected_template: Optional[SchemaTemplate] = None
        self.selected_template_id: Optional[str] = None
        self._setup_template_ui()

    def _setup_template_ui(self):
        """Setup the template selection UI"""
        # Minimalist layout - no nested boxes
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Schema name input at top
        name_container = QWidget()
        name_container.setStyleSheet(
            """
            QWidget {
                background-color: #FFFFFF;
                border-bottom: 2px solid #000000;
            }
        """
        )
        name_layout = QHBoxLayout(name_container)
        name_layout.setContentsMargins(20, 12, 20, 12)

        name_label = QLabel("SCHEMA NAME:")
        name_label.setStyleSheet("font-weight: 600; font-size: 14px;")

        self.schema_name_input = QLineEdit()
        self.schema_name_input.setPlaceholderText(
            "Schema name will be set automatically when template is selected"
        )
        self.schema_name_input.setStyleSheet(
            """
            QLineEdit {
                border: none;
                border-bottom: 1px solid #000;
                padding: 4px 0;
                background: transparent;
                font-size: 16px;
            }
        """
        )
        self.schema_name_input.textChanged.connect(self._update_apply_button)

        name_layout.addWidget(name_label)
        name_layout.addWidget(self.schema_name_input, 1)

        main_layout.addWidget(name_container)

        # Main content area - side by side
        content_layout = QHBoxLayout()
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Left: Template list
        left_panel = self._create_minimal_template_list()
        content_layout.addWidget(left_panel, 2)

        # Vertical divider
        divider = QFrame()
        divider.setFrameShape(QFrame.VLine)
        divider.setStyleSheet("background-color: #000; max-width: 2px;")
        content_layout.addWidget(divider)

        # Right: Preview
        right_panel = self._create_minimal_preview()
        content_layout.addWidget(right_panel, 3)

        main_layout.addLayout(content_layout, 1)

        # Bottom action bar
        action_bar = QWidget()
        action_bar.setStyleSheet(
            """
            QWidget {
                background-color: #F5F5F5;
                border-top: 2px solid #000000;
            }
        """
        )
        action_layout = QHBoxLayout(action_bar)
        action_layout.setContentsMargins(20, 8, 20, 8)

        cancel_btn = QPushButton("CANCEL")
        cancel_btn.setStyleSheet(
            """
            QPushButton {
                background: white;
                border: 1px solid black;
                padding: 6px 20px;
                font-size: 13px;
                font-weight: 500;
                min-height: 32px;
            }
            QPushButton:hover {
                background: #F0F0F0;
            }
        """
        )
        cancel_btn.clicked.connect(self.reject)

        self.apply_btn = QPushButton("APPLY")
        self.apply_btn.setEnabled(False)
        self.apply_btn.setStyleSheet(
            """
            QPushButton {
                background: black;
                color: white;
                border: 1px solid black;
                padding: 6px 20px;
                font-size: 13px;
                font-weight: 500;
                min-height: 32px;
            }
            QPushButton:hover:enabled {
                background: #333;
            }
            QPushButton:disabled {
                background: #CCC;
                border-color: #CCC;
            }
        """
        )
        self.apply_btn.clicked.connect(self._apply_template)

        action_layout.addStretch()
        action_layout.addWidget(cancel_btn)
        action_layout.addWidget(self.apply_btn)

        main_layout.addWidget(action_bar)

        self.content_layout.addLayout(main_layout)

        # Set dialog size
        self.setMinimumSize(900, 600)
        self.setMaximumSize(900, 600)

    def _create_minimal_template_list(self) -> QWidget:
        """Create minimalist template list"""
        container = QWidget()
        container.setStyleSheet("background: #FAFAFA;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header
        header = QLabel("TEMPLATES")
        header.setStyleSheet(
            """
            QLabel {
                font-size: 13px;
                font-weight: 600;
                padding: 16px 20px;
                border-bottom: 1px solid #E0E0E0;
            }
        """
        )
        layout.addWidget(header)

        # Template list
        self.template_list = QListWidget()
        self.template_list.setStyleSheet(
            """
            QListWidget {
                border: none;
                background: transparent;
                outline: none;
            }
            QListWidget::item {
                padding: 16px 20px;
                border-bottom: 1px solid #E0E0E0;
            }
            QListWidget::item:hover {
                background: #F0F0F0;
            }
            QListWidget::item:selected {
                background: #000;
                color: white;
            }
        """
        )

        # Add templates
        for template_id in self.template_manager.list_templates():
            template_info = self.template_manager.get_template_info(template_id)
            metadata = template_info["metadata"]
            item = QListWidgetItem()

            # Simple text layout
            item_widget = QWidget()
            item_layout = QVBoxLayout(item_widget)
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(4)

            name_label = QLabel(metadata.name.upper())
            name_label.setStyleSheet("font-weight: 500; font-size: 14px;")

            desc_label = QLabel(metadata.description)
            desc_label.setStyleSheet("font-size: 12px; color: #666;")

            item_layout.addWidget(name_label)
            item_layout.addWidget(desc_label)

            item.setSizeHint(QSize(0, 70))
            self.template_list.addItem(item)
            self.template_list.setItemWidget(item, item_widget)
            item.setData(Qt.UserRole, template_id)

        self.template_list.itemClicked.connect(self._on_template_selected)
        layout.addWidget(self.template_list)

        return container

    def _create_minimal_preview(self) -> QWidget:
        """Create minimalist preview panel"""
        container = QWidget()
        container.setStyleSheet("background: white;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 0, 20, 20)
        layout.setSpacing(0)

        # Header with copy button
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 16, 0, 16)

        header = QLabel("JSON PREVIEW")
        header.setStyleSheet(
            """
            QLabel {
                font-size: 13px;
                font-weight: 600;
            }
        """
        )
        header_layout.addWidget(header)

        self.copy_btn = QPushButton("COPY")
        self.copy_btn.setEnabled(False)
        self.copy_btn.setStyleSheet(
            """
            QPushButton {
                border: 1px solid black;
                background: white;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 500;
                min-height: 24px;
            }
            QPushButton:hover:enabled {
                background: #F0F0F0;
            }
            QPushButton:disabled {
                border-color: #CCC;
                color: #999;
            }
        """
        )
        self.copy_btn.clicked.connect(self._copy_preview)
        header_layout.addWidget(self.copy_btn)

        header_layout.addStretch()
        layout.addLayout(header_layout)

        # Preview area
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setFont(QFont("Consolas", 10))
        self.preview_text.setStyleSheet(
            """
            QTextEdit {
                border: 1px solid #E0E0E0;
                background: #FAFAFA;
                padding: 16px;
            }
        """
        )
        self.preview_text.setPlaceholderText(
            "Select a template to preview JSON structure"
        )
        layout.addWidget(self.preview_text, 1)

        # Info bar
        self.info_label = QLabel()
        self.info_label.setStyleSheet(
            """
            QLabel {
                background: #F5F5F5;
                border: 1px solid #E0E0E0;
                padding: 8px 16px;
                font-size: 12px;
                color: #666;
                margin-top: 16px;
            }
        """
        )
        self.info_label.setWordWrap(True)
        self.info_label.setVisible(False)
        layout.addWidget(self.info_label)

        return container

    def _on_template_selected(self, item):
        """Handle template selection"""
        template_id = item.data(Qt.UserRole)
        template = self.template_manager.get_template(template_id)

        if template:
            self.selected_template = template
            self.selected_template_id = template_id

            # Automatically set schema name to template metadata name
            schema_name = template.metadata.name
            self.schema_name_input.setText(schema_name)

            # Update preview
            preview_data = {schema_name: template.to_preview_data()}
            json_str = json.dumps(preview_data, indent=2, ensure_ascii=False)
            self.preview_text.setText(json_str)

            # Show template info
            self._show_template_info(template)

            # Enable copy button
            self.copy_btn.setEnabled(True)

            # Update apply button
            self._update_apply_button()

    def _show_template_info(self, template: SchemaTemplate):
        """Show template information"""
        var_counts = {}
        for var_type in [
            "basic_variables",
            "more_variables",
            "image_variables",
            "url_variables",
            "array_variables",
            "language_item_variables",
        ]:
            count = len(template.to_preview_data().get(var_type, []))
            if count > 0:
                var_counts[var_type.replace("_", " ").title()] = count

        info_parts = [f"{count} {var_type}" for var_type, count in var_counts.items()]
        info_text = "Contains: " + ", ".join(info_parts)

        self.info_label.setText(info_text)
        self.info_label.setVisible(True)

    def _update_apply_button(self):
        """Update apply button state"""
        self.apply_btn.setEnabled(self.selected_template is not None)

    def _copy_preview(self):
        """Copy preview JSON to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.preview_text.toPlainText())

        # Show feedback
        self.copy_btn.setText("COPIED")
        QTimer.singleShot(1000, lambda: self.copy_btn.setText("COPY"))

    def _apply_template(self):
        """Apply the selected template"""
        if self.selected_template:
            self.accept()

    def get_schema_from_template(self):
        """Get schema created from selected template"""
        if self.selected_template:
            schema_name = self.schema_name_input.text().strip()
            return self.selected_template.to_schema(schema_name)
        return None
