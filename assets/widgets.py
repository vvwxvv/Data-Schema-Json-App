from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AnimatedButton(QPushButton):
    """Button with smooth animations"""

    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(250)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

    def enterEvent(self, event):
        super().enterEvent(event)

    def leaveEvent(self, event):
        super().leaveEvent(event)


class Card(QFrame):
    """Elegant card component with shadow"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")

        # Add subtle shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow)


class FadeInWidget(QWidget):
    """Widget that fades in when shown"""

    def __init__(self, parent=None):
        super().__init__(parent)
        effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(effect)
        self.fade_animation = QPropertyAnimation(effect, b"opacity")
        self.fade_animation.setDuration(350)
        self.fade_animation.setStartValue(0)
        self.fade_animation.setEndValue(1)

    def showEvent(self, event):
        super().showEvent(event)
        self.fade_animation.start()
