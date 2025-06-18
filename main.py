import sys
import logging
from PyQt5.QtWidgets import QApplication
from assets.main_window import MainWindow

# Logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def main():
    """Application entry point"""
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName("Schema Designer Pro")
    app.setOrganizationName("YourCompany")

    # Set fusion style for better cross-platform look
    app.setStyle("Fusion")

    # Create and show main window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
