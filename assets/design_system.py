class DesignSystem:
    """Centralized design tokens for consistent UI"""

    class Colors:
        # ===== LIGHT MODE COLORS =====
        # Primary Palette
        BLACK = "#000000"
        WHITE = "#FFFFFF"

        # Grayscale (Light Mode)
        GRAY_900 = "#0A0A0A"  # Near black
        GRAY_800 = "#1A1A1A"  # Very dark gray
        GRAY_700 = "#2E2E2E"  # Dark gray
        GRAY_600 = "#404040"  # Medium dark gray
        GRAY_500 = "#6B6B6B"  # Medium gray
        GRAY_400 = "#9CA3AF"  # Medium light gray
        GRAY_300 = "#D1D5DB"  # Light gray
        GRAY_200 = "#E5E7EB"  # Very light gray
        GRAY_100 = "#F3F4F6"  # Near white gray
        GRAY_50 = "#F9FAFB"  # Off white

        # Semantic Colors (Monochrome)
        PRIMARY = BLACK
        SECONDARY = GRAY_700
        BACKGROUND = WHITE
        SURFACE = GRAY_50
        BORDER = GRAY_400  # Darker for better visibility
        TEXT_PRIMARY = GRAY_900
        TEXT_SECONDARY = GRAY_600
        TEXT_DISABLED = GRAY_400

        # Status Colors (Grayscale variants)
        ERROR = GRAY_900  # Black for errors
        SUCCESS = GRAY_700  # Dark gray for success
        WARNING = GRAY_600  # Medium gray for warnings
        INFO = GRAY_500  # Gray for info

        # Interactive States
        HOVER = GRAY_100
        ACTIVE = GRAY_200
        FOCUS = BLACK

        # ===== DARK MODE COLORS =====
        # Dark mode palette
        DARK_BG = "#0F0F0F"
        DARK_SURFACE = "#1A1A1A"
        DARK_SURFACE_2 = "#242424"
        DARK_SURFACE_3 = "#2E2E2E"
        DARK_BORDER = "#505050"
        DARK_TEXT_PRIMARY = "#F0F0F0"
        DARK_TEXT_SECONDARY = "#B0B0B0"
        DARK_TEXT_DISABLED = "#606060"

    class Typography:
        # Font Families
        FONT_PRIMARY = "'Inter', 'Segoe UI', 'Roboto', Arial, sans-serif"
        FONT_MONO = "'JetBrains Mono', 'Consolas', 'Monaco', monospace"

        # Font Sizes - Optimized for readability
        SIZE_XS = "14px"
        SIZE_SM = "16px"
        SIZE_BASE = "18px"
        SIZE_LG = "20px"
        SIZE_XL = "24px"
        SIZE_2XL = "32px"
        SIZE_3XL = "40px"

        # Font Weights
        WEIGHT_LIGHT = "300"
        WEIGHT_NORMAL = "400"
        WEIGHT_MEDIUM = "500"
        WEIGHT_SEMIBOLD = "600"
        WEIGHT_BOLD = "700"

    class Spacing:
        XS = "4px"
        SM = "8px"
        MD = "16px"
        LG = "20px"
        XL = "28px"
        XXL = "36px"
        XXXL = "48px"

    class BorderRadius:
        NONE = "0px"
        SM = "6px"
        MD = "10px"
        LG = "14px"
        XL = "18px"
        XXL = "24px"
        FULL = "9999px"

    class Border:
        # Border widths
        THIN = "2px"
        MEDIUM = "3px"
        THICK = "4px"


class StyleSheets:
    """Centralized stylesheets for the application with dark mode support"""

    @staticmethod
    def get_application_style(dark_mode: bool = False) -> str:
        """Returns the main application stylesheet"""
        ds = DesignSystem

        # Dynamic color selection based on mode
        bg_color = ds.Colors.DARK_BG if dark_mode else ds.Colors.BACKGROUND
        surface_color = ds.Colors.DARK_SURFACE if dark_mode else ds.Colors.SURFACE
        surface_color_2 = ds.Colors.DARK_SURFACE_2 if dark_mode else ds.Colors.WHITE
        border_color = ds.Colors.DARK_BORDER if dark_mode else ds.Colors.BORDER
        text_primary = (
            ds.Colors.DARK_TEXT_PRIMARY if dark_mode else ds.Colors.TEXT_PRIMARY
        )
        text_secondary = (
            ds.Colors.DARK_TEXT_SECONDARY if dark_mode else ds.Colors.TEXT_SECONDARY
        )
        text_disabled = (
            ds.Colors.DARK_TEXT_DISABLED if dark_mode else ds.Colors.TEXT_DISABLED
        )

        return f"""
        /* ========================================
           GLOBAL BASE STYLES
           ======================================== */
        QWidget {{
            background-color: {bg_color};
            color: {text_primary};
            font-family: {ds.Typography.FONT_PRIMARY};
            font-size: {ds.Typography.SIZE_BASE};
            font-weight: {ds.Typography.WEIGHT_NORMAL};
        }}
        
        /* ========================================
           MAIN WINDOW
           ======================================== */
        QMainWindow {{
            background-color: {bg_color};
        }}
        
        /* ========================================
           SCROLLBARS - Minimal Design
           ======================================== */
        QScrollBar:vertical {{
            background: {surface_color};
            width: 14px;
            border-radius: 7px;
            margin: 0;
            border: none;
        }}
        
        QScrollBar::handle:vertical {{
            background: {ds.Colors.GRAY_400 if not dark_mode else ds.Colors.GRAY_600};
            border-radius: 7px;
            min-height: 30px;
            margin: 2px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background: {ds.Colors.GRAY_500 if not dark_mode else ds.Colors.GRAY_500};
        }}
        
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0;
            background: none;
        }}
        
        /* Horizontal Scrollbar */
        QScrollBar:horizontal {{
            background: {surface_color};
            height: 14px;
            border-radius: 7px;
            margin: 0;
            border: none;
        }}
        
        QScrollBar::handle:horizontal {{
            background: {ds.Colors.GRAY_400 if not dark_mode else ds.Colors.GRAY_600};
            border-radius: 7px;
            min-width: 30px;
            margin: 2px;
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background: {ds.Colors.GRAY_500 if not dark_mode else ds.Colors.GRAY_500};
        }}
        
        /* ========================================
           LABELS & HEADINGS
           ======================================== */
        QLabel {{
            color: {text_primary};
            background: transparent;
            font-size: {ds.Typography.SIZE_BASE};
        }}
        
        /* Large Display Heading */
        QLabel#heading1 {{
            font-size: {ds.Typography.SIZE_3XL};
            font-weight: {ds.Typography.WEIGHT_LIGHT};
            color: {text_primary};
            margin-bottom: {ds.Spacing.MD};
        }}
        
        /* Section Heading */
        QLabel#heading2 {{
            font-size: {ds.Typography.SIZE_2XL};
            font-weight: {ds.Typography.WEIGHT_SEMIBOLD};
            color: {text_primary};
            margin-bottom: {ds.Spacing.SM};
        }}
        
        /* Subsection Heading */
        QLabel#heading3 {{
            font-size: {ds.Typography.SIZE_XL};
            font-weight: {ds.Typography.WEIGHT_MEDIUM};
            color: {text_primary};
        }}
        
        /* Caption Text */
        QLabel#caption {{
            font-size: {ds.Typography.SIZE_SM};
            font-weight: {ds.Typography.WEIGHT_NORMAL};
            color: {text_secondary};
        }}
        
        /* Error Text */
        QLabel#error {{
            color: {text_primary};
            font-size: {ds.Typography.SIZE_SM};
            font-weight: {ds.Typography.WEIGHT_MEDIUM};
        }}
        
        /* ========================================
           BUTTONS - Monochrome Design
           ======================================== */
        
        /* Minimalist German/Nordic Button Style */
        QPushButton {{
            font-size: {ds.Typography.SIZE_SM};
            font-weight: {ds.Typography.WEIGHT_MEDIUM};
            padding: 8px 16px;
            background-color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
            color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            border: 2px solid {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            border-radius: 0;  /* No rounded corners for strict design */
            min-height: 36px;  /* Reduced height */
            max-height: 36px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        QPushButton:hover {{
            background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
        }}
        
        QPushButton:pressed {{
            background-color: {ds.Colors.GRAY_700 if not dark_mode else ds.Colors.GRAY_300};
        }}
        
        QPushButton:disabled {{
            background-color: {ds.Colors.GRAY_200};
            color: {text_disabled};
        }}
        
        /* Secondary Button - Medium Emphasis */
        QPushButton#secondary {{
            background-color: {surface_color_2};
            color: {text_primary};
            border: {ds.Border.MEDIUM} solid {border_color};
        }}
        
        QPushButton#secondary:hover {{
            background-color: {ds.Colors.GRAY_100 if not dark_mode else ds.Colors.DARK_SURFACE_3};
            border-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        /* Ghost Button - Low Emphasis */
        QPushButton#ghost {{
            background-color: transparent;
            color: {text_primary};
            border: none;
            text-transform: none;
        }}
        
        QPushButton#ghost:hover {{
            background-color: {ds.Colors.GRAY_100 if not dark_mode else ds.Colors.DARK_SURFACE_3};
        }}
        
        /* Success Button */
        QPushButton#success {{
            background-color: {ds.Colors.GRAY_700 if not dark_mode else ds.Colors.GRAY_300};
            color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
        }}
        
        QPushButton#success:hover {{
            background-color: {ds.Colors.GRAY_800 if not dark_mode else ds.Colors.GRAY_200};
        }}
        
        /* Danger Button */
        QPushButton#danger {{
            background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
            border: {ds.Border.MEDIUM} solid {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        QPushButton#danger:hover {{
            background-color: {ds.Colors.GRAY_900 if not dark_mode else ds.Colors.GRAY_100};
        }}
        
        /* Warning Button */
        QPushButton#warning {{
            background-color: {ds.Colors.GRAY_600 if not dark_mode else ds.Colors.GRAY_400};
            color: {ds.Colors.WHITE};
        }}
        
        QPushButton#warning:hover {{
            background-color: {ds.Colors.GRAY_700 if not dark_mode else ds.Colors.GRAY_300};
        }}
        
        /* ========================================
           INPUT FIELDS
           ======================================== */
        QLineEdit, QTextEdit, QSpinBox {{
            font-size: {ds.Typography.SIZE_BASE};
            padding: {ds.Spacing.MD} {ds.Spacing.LG};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.MD};
            background-color: {surface_color_2};
            color: {text_primary};
            min-height: 48px;
        }}
        
        QLineEdit:hover, QTextEdit:hover, QSpinBox:hover {{
            border-color: {ds.Colors.GRAY_500 if not dark_mode else ds.Colors.GRAY_400};
            background-color: {surface_color if not dark_mode else ds.Colors.DARK_SURFACE_2};
        }}
        
        QLineEdit:focus, QTextEdit:focus, QSpinBox:focus {{
            border-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            outline: none;
        }}
        
        QLineEdit:disabled, QTextEdit:disabled, QSpinBox:disabled {{
            background-color: {surface_color};
            color: {text_disabled};
            border-color: {ds.Colors.GRAY_200 if not dark_mode else ds.Colors.DARK_BORDER};
        }}
        
        /* Text Edit - Monospace Font */
        QTextEdit {{
            font-family: {ds.Typography.FONT_MONO};
            font-size: {ds.Typography.SIZE_SM};
        }}
        
        /* ========================================
           SPIN BOX ARROWS
           ======================================== */
        QSpinBox::up-button, QSpinBox::down-button {{
            width: 30px;
            border: none;
            background-color: {surface_color};
            border-radius: {ds.BorderRadius.SM};
            margin: 2px;
        }}
        
        QSpinBox::up-button:hover, QSpinBox::down-button:hover {{
            background-color: {ds.Colors.GRAY_200 if not dark_mode else ds.Colors.DARK_SURFACE_3};
        }}
        
        /* ========================================
           COMBO BOX
           ======================================== */
        QComboBox {{
            font-size: {ds.Typography.SIZE_BASE};
            padding: {ds.Spacing.MD} {ds.Spacing.LG};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.MD};
            background-color: {surface_color_2};
            color: {text_primary};
            min-height: 48px;
        }}
        
        QComboBox:hover {{
            border-color: {ds.Colors.GRAY_500 if not dark_mode else ds.Colors.GRAY_400};
        }}
        
        QComboBox:focus {{
            border-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 40px;
            background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            border-top-right-radius: {ds.BorderRadius.MD};
            border-bottom-right-radius: {ds.BorderRadius.MD};
        }}
        
        QComboBox::down-arrow {{
            image: none;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 6px solid {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {surface_color_2};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.MD};
            selection-background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            selection-color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
            padding: {ds.Spacing.SM};
            font-size: {ds.Typography.SIZE_BASE};
        }}
        
        /* ========================================
           LIST WIDGET
           ======================================== */
        QListWidget {{
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.LG};
            background-color: {surface_color_2};
            padding: {ds.Spacing.SM};
            outline: none;
            font-size: {ds.Typography.SIZE_BASE};
        }}
        
        QListWidget::item {{
            padding: {ds.Spacing.MD};
            border-radius: {ds.BorderRadius.MD};
            margin-bottom: {ds.Spacing.XS};
            min-height: 40px;
            border: {ds.Border.THIN} solid transparent;
        }}
        
        QListWidget::item:hover {{
            background-color: {ds.Colors.GRAY_100 if not dark_mode else ds.Colors.DARK_SURFACE_3};
            border-color: {ds.Colors.GRAY_300 if not dark_mode else ds.Colors.DARK_BORDER};
        }}
        
        QListWidget::item:selected {{
            background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
            border-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        /* ========================================
           TAB WIDGET
           ======================================== */
        QTabWidget::pane {{
            background-color: {surface_color_2};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.LG};
            border-top-left-radius: 0;
            padding: {ds.Spacing.LG};
        }}
        
        QTabBar::tab {{
            background-color: {surface_color};
            padding: {ds.Spacing.MD} {ds.Spacing.XL};
            color: {text_secondary};
            font-weight: {ds.Typography.WEIGHT_MEDIUM};
            font-size: {ds.Typography.SIZE_BASE};
            border-bottom: {ds.Border.THICK} solid transparent;
            margin-right: {ds.Spacing.SM};
            min-height: 48px;
            border-top-left-radius: {ds.BorderRadius.MD};
            border-top-right-radius: {ds.BorderRadius.MD};
        }}
        
        QTabBar::tab:selected {{
            color: {text_primary};
            background-color: {surface_color_2};
            border-bottom-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        QTabBar::tab:hover:!selected {{
            color: {text_primary};
            background-color: {ds.Colors.GRAY_100 if not dark_mode else ds.Colors.DARK_SURFACE_3};
        }}
        
        /* ========================================
           GROUP BOX
           ======================================== */
        QGroupBox {{
            font-size: {ds.Typography.SIZE_LG};
            font-weight: {ds.Typography.WEIGHT_MEDIUM};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.LG};
            margin-top: {ds.Spacing.XL};
            padding-top: {ds.Spacing.XL};
            background-color: {surface_color_2};
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: {ds.Spacing.LG};
            padding: 0 {ds.Spacing.SM};
            background-color: {surface_color_2};
            color: {text_primary};
        }}
        
        /* ========================================
           CARDS
           ======================================== */
        QFrame#card {{
            background-color: {surface_color_2};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.LG};
        }}
        
        /* ========================================
           DIALOGS
           ======================================== */
        QDialog {{
            background-color: {surface_color_2};
            border-radius: {ds.BorderRadius.XL};
        }}
        
        /* ========================================
           TOOL BUTTONS - Icon Buttons
           ======================================== */
        QToolButton {{
            background-color: transparent;
            border: none;
            border-radius: {ds.BorderRadius.FULL};
            padding: {ds.Spacing.MD};
            color: {text_secondary};
            font-size: {ds.Typography.SIZE_XL};
            min-width: 48px;
            min-height: 48px;
        }}
        
        QToolButton:hover {{
            background-color: {ds.Colors.GRAY_100 if not dark_mode else ds.Colors.DARK_SURFACE_3};
            color: {text_primary};
        }}
        
        QToolButton:pressed {{
            background-color: {ds.Colors.GRAY_200 if not dark_mode else ds.Colors.DARK_SURFACE_2};
        }}
        
        /* Dark Mode Toggle Button */
        QToolButton#darkModeToggle {{
            background-color: {ds.Colors.GRAY_200 if not dark_mode else ds.Colors.DARK_SURFACE_3};
            border: {ds.Border.MEDIUM} solid {border_color};
        }}
        
        QToolButton#darkModeToggle:hover {{
            background-color: {ds.Colors.GRAY_300 if not dark_mode else ds.Colors.DARK_SURFACE_2};
            border-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        /* ========================================
           STATUS BAR
           ======================================== */
        QStatusBar {{
            background-color: {surface_color};
            color: {text_secondary};
            border-top: {ds.Border.THIN} solid {border_color};
            padding: {ds.Spacing.SM} {ds.Spacing.LG};
            font-size: {ds.Typography.SIZE_SM};
        }}
        
        /* ========================================
           SPLITTER HANDLES
           ======================================== */
        QSplitter::handle {{
            background-color: {border_color};
            border-radius: {ds.BorderRadius.SM};
        }}
        
        QSplitter::handle:horizontal {{
            width: {ds.Border.THICK};
            margin: {ds.Spacing.MD} 0;
        }}
        
        QSplitter::handle:vertical {{
            height: {ds.Border.THICK};
            margin: 0 {ds.Spacing.MD};
        }}
        
        QSplitter::handle:hover {{
            background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
        }}
        
        /* ========================================
           MESSAGE BOX
           ======================================== */
        QMessageBox {{
            background-color: {surface_color_2};
        }}
        
        QMessageBox QLabel {{
            color: {text_primary};
            font-size: {ds.Typography.SIZE_BASE};
        }}
        
        QMessageBox QPushButton {{
            min-width: 100px;
        }}
        
        /* ========================================
           FORM LAYOUT
           ======================================== */
        QFormLayout QLabel {{
            font-size: {ds.Typography.SIZE_BASE};
            font-weight: {ds.Typography.WEIGHT_MEDIUM};
        }}
        
        /* ========================================
           MENU
           ======================================== */
        QMenu {{
            background-color: {surface_color_2};
            border: {ds.Border.MEDIUM} solid {border_color};
            border-radius: {ds.BorderRadius.MD};
            padding: {ds.Spacing.SM} 0;
        }}
        
        QMenu::item {{
            padding: {ds.Spacing.MD} {ds.Spacing.XL};
            font-size: {ds.Typography.SIZE_BASE};
            min-height: 36px;
        }}
        
        QMenu::item:selected {{
            background-color: {ds.Colors.BLACK if not dark_mode else ds.Colors.WHITE};
            color: {ds.Colors.WHITE if not dark_mode else ds.Colors.BLACK};
        }}
        
        QMenu::separator {{
            height: {ds.Border.THIN};
            background-color: {border_color};
            margin: {ds.Spacing.SM} {ds.Spacing.LG};
        }}
        """
