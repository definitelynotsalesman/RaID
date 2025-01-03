from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QMessageBox, QWidget,  QVBoxLayout, QLineEdit, QLabel
from PyQt6.QtGui import QPixmap, QCursor, QIcon, QColor
from PyQt6.QtCore import Qt, QEvent

class SangriaDye(QPushButton):
    def __init__(self, image_path, name, x, y, parent = None):
        super().__init__(parent)
        self.image_path = image_path
        self.name = name
        self.setIcon(QIcon(QPixmap(image_path)))
        self.setIconSize(QPixmap(image_path).scaled(50,50).size())
        self.resize(47,47)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)            
        shadow.setColor(QColor(0, 0, 0, 150)) 
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("""
            QPushButton {
                background-color: #4A4A4A;  /* Dark grey */
                border-radius: 8px;         /* Slightly rounded corners */
                padding: 5px;
                border: none;               /* No border by default */
            }
            QPushButton:hover {
                background-color: #2E2E2E;  /* Darker grey on hover */
                border: 1px solid #2E2E2E;  /* Border matches hover background */
            }
            QPushButton:pressed {
                background-color: #1A1A1A;  /* Darker grey when pressed */
                border: 1px solid #1A1A1A;  /* Border matches pressed background */
            }
        """)
        self.move(x,y)

    def getName(self):
        return self.name
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIconPixmap(QPixmap(self.image_path))
            msg.exec()

class CeladonDye(QPushButton):
    def __init__(self, image_path, name, x, y, parent = None):
        super().__init__(parent)
        self.image_path = image_path
        self.name = name
        self.setIcon(QIcon(QPixmap(image_path)))
        self.setIconSize(QPixmap(image_path).scaled(50,50).size())
        self.resize(47,47)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)            
        shadow.setColor(QColor(0, 0, 0, 150)) 
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("""
            QPushButton {
                background-color: #4A4A4A;  /* Dark grey */
                border-radius: 8px;         /* Slightly rounded corners */
                padding: 5px;
                border: none;               /* No border by default */
            }
            QPushButton:hover {
                background-color: #2E2E2E;  /* Darker grey on hover */
                border: 1px solid #2E2E2E;  /* Border matches hover background */
            }
            QPushButton:pressed {
                background-color: #1A1A1A;  /* Darker grey when pressed */
                border: 1px solid #1A1A1A;  /* Border matches pressed background */
            }
        """)
        self.move(x,y)

    def getName(self):
        return self.name

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIconPixmap(QPixmap(self.image_path))
            msg.exec()

class IcebergDye(QPushButton):
    def __init__(self, image_path, name, x, y, parent = None):
        super().__init__(parent)
        self.image_path = image_path
        self.name = name
        self.setIcon(QIcon(QPixmap(image_path)))
        self.setIconSize(QPixmap(image_path).scaled(50,50).size())
        self.resize(47,47)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)            
        shadow.setColor(QColor(0, 0, 0, 150)) 
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("""
            QPushButton {
                background-color: #4A4A4A;  /* Dark grey */
                border-radius: 8px;         /* Slightly rounded corners */
                padding: 5px;
                border: none;               /* No border by default */
            }
            QPushButton:hover {
                background-color: #2E2E2E;  /* Darker grey on hover */
                border: 1px solid #2E2E2E;  /* Border matches hover background */
            }
            QPushButton:pressed {
                background-color: #1A1A1A;  /* Darker grey when pressed */
                border: 1px solid #1A1A1A;  /* Border matches pressed background */
            }
        """)
        self.move(x,y)
    def getName(self):
        return self.name
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIconPixmap(QPixmap(self.image_path))
            msg.exec()

class AquamarineDye(QPushButton):
    def __init__(self, image_path, name, x, y, parent = None):
        super().__init__(parent)
        self.image_path = image_path
        self.name = name

        self.setIcon(QIcon(QPixmap(image_path)))
        self.setIconSize(QPixmap(image_path).scaled(50,50).size())
        self.resize(47,47)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)            
        shadow.setColor(QColor(0, 0, 0, 150)) 
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("""
            QPushButton {
                background-color: #4A4A4A;  /* Dark grey */
                border-radius: 8px;         /* Slightly rounded corners */
                padding: 5px;
                border: none;               /* No border by default */
            }
            QPushButton:hover {
                background-color: #2E2E2E;  /* Darker grey on hover */
                border: 1px solid #2E2E2E;  /* Border matches hover background */
            }
            QPushButton:pressed {
                background-color: #1A1A1A;  /* Darker grey when pressed */
                border: 1px solid #1A1A1A;  /* Border matches pressed background */
            }
        """)
        self.move(x,y)

    def getName(self):
        return self.name
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIconPixmap(QPixmap(self.image_path))
            msg.exec()



