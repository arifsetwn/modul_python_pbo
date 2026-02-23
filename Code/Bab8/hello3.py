from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hello PyQt6')
        self.button = QPushButton('Click Me!')
        self.button.clicked.connect(self.show_message)
        self.setCentralWidget(self.button)


    def show_message(self):
        QMessageBox.information(self, 'Information', 'Hello, PyQt6!')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
