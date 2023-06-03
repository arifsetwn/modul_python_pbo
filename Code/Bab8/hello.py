from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([]) #ini object dari QApplication

label = QLabel('Hello PyQt!') #Widget Text

label.show() #menampilkan

app.exec_()