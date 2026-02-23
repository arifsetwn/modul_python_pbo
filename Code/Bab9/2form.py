from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.button = QPushButton("Open Dialog", self)
        self.button.clicked.connect(self.open_dialog)

    def open_dialog(self):
        self.dialog = DialogWindow()
        self.dialog.show()

class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialog Window')

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
