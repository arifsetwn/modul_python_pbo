from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

def show_message():
    QMessageBox.information(window, 'Information', 'Hello, PyQt6!')

app = QApplication([]) #ini object dari QApplication
window = QMainWindow()
button = QPushButton('Click Me!')
button.clicked.connect(show_message)
window.setCentralWidget(button)
window.show()
app.exec()