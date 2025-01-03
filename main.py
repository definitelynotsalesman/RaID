from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
from Widgets import SangriaDye, CeladonDye, IcebergDye

from api import refresh_ah
app = QApplication([])

window = QWidget()
window.setWindowTitle("Dyes")
window.setFixedSize(800, 800)

timer = QTimer()
timer.timeout.connect(refresh_ah) #add api function here
timer.start(1000 * 15 * 60)

sangria_dye = SangriaDye("/Users/akaei/Desktop/RaID/resources/Sangria_Dye.webp", "SANGRIA_DYE", 50, 50, window)
celadon_dye = CeladonDye("/Users/akaei/Desktop/RaID/resources/Celadon_Dye.webp", "CELADON_DYE", 150, 50, window)
iceberg_dye = IcebergDye("/Users/akaei/Desktop/RaID/resources/Iceberg_Dye.webp", "ICEBERG_DYE", 250, 50, window)

window.show()
app.exec()  
