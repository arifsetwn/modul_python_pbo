from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([]) #ini object dari QApplication
window = QMainWindow()
button = QPushButton('Click Me!')
window.setCentralWidget(button)
window.show()
app.exec()