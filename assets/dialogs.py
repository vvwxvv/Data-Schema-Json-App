from typing import Optional
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .models import Variable
from .widgets import Card


class ModernDialog(QDialog):
    """Base class for modern-styled dialogs"""

    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumWidth(500)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self._setup_ui(title)

    def _setup_ui(self, title: str):
        """Setup the dialog UI"""
        # Main container
        self.container = Card()
        container_layout = QVBoxLayout(self.container)
        container_layout.setContentsMargins(32, 32, 32, 32)
        container_layout.setSpacing(24)

        # Header
        header_layout = QHBoxLayout()

        title_label = QLabel(title)
        title_label.setObjectName("heading2")
        header_layout.addWidget(title_label)
        header_layout.addStretch()

        # Close button
        close_btn = QToolButton()
        close_btn.setText("✕")
        close_btn.setStyleSheet(
            """
            QToolButton {
                font-size: 18px;
                color: #6B6B6B;
                background: transparent;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QToolButton:hover {
                background-color: #F3F4F6;
                color: #000000;
            }
        """
        )
        close_btn.clicked.connect(self.reject)
        header_layout.addWidget(close_btn)

        container_layout.addLayout(header_layout)

        # Content area
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.addWidget(self.content_widget, 1)

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.container)

    def mousePressEvent(self, event):
        """Handle mouse press for dragging"""
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging"""
        if event.buttons() == Qt.LeftButton and hasattr(self, "drag_pos"):
            self.move(event.globalPos() - self.drag_pos)


class VariableDialog(ModernDialog):
    """Dialog for adding/editing variables"""

    def __init__(self, var_type: str, variable: Optional[Variable] = None, parent=None):
        self.var_type = var_type
        self.variable = variable
        super().__init__(f"{'Edit' if variable else 'Add'} {var_type}")
        self._setup_form()

    def _setup_form(self):
        """Setup the form fields"""
        form_layout = QFormLayout()
        form_layout.setSpacing(20)
        form_layout.setLabelAlignment(Qt.AlignRight)

        # Variable name
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g., user_name, product_id")
        if self.variable:
            self.name_input.setText(self.variable.name)
        form_layout.addRow("Variable Name *", self.name_input)

        # English text
        self.en_input = QLineEdit()
        self.en_input.setPlaceholderText("Display text in English")
        if self.variable:
            self.en_input.setText(self.variable.en_text)
        form_layout.addRow("English Text", self.en_input)

        # Chinese text
        self.cn_input = QLineEdit()
        self.cn_input.setPlaceholderText("中文显示文本")
        if self.variable:
            self.cn_input.setText(self.variable.cn_text)
        form_layout.addRow("Chinese Text", self.cn_input)

        # Number of rows
        self.rows_input = QSpinBox()
        self.rows_input.setRange(0, 9999)
        if self.variable:
            self.rows_input.setValue(self.variable.rows)
        form_layout.addRow("Number of Rows", self.rows_input)

        self.content_layout.addLayout(form_layout)
        self.content_layout.addStretch()

        # Error label
        self.error_label = QLabel()
        self.error_label.setObjectName("error")
        self.error_label.setVisible(False)
        self.content_layout.addWidget(self.error_label)

        # Action buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)

        cancel_btn = QPushButton("CANCEL")
        cancel_btn.setObjectName("secondary")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("SAVE" if self.variable else "ADD")
        save_btn.clicked.connect(self._validate_and_accept)
        save_btn.setDefault(True)

        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)

        self.content_layout.addLayout(button_layout)

        # Focus
        self.name_input.setFocus()

    def _validate_and_accept(self):
        """Validate inputs and accept dialog"""
        name = self.name_input.text().strip()

        if not name:
            self.error_label.setText("Variable name is required")
            self.error_label.setVisible(True)
            self.name_input.setFocus()
            return

        self.variable = Variable(
            name=name,
            en_text=self.en_input.text().strip(),
            cn_text=self.cn_input.text().strip(),
            rows=self.rows_input.value(),
        )
        self.accept()

    def get_variable(self) -> Optional[Variable]:
        """Get the variable data"""
        return self.variable
