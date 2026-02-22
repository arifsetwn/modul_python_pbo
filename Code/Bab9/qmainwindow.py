from PyQt5.QtWidgets import QApplication, QMainWindow 

class MainWindow(QMainWindow):      
    def __init__(self): 
     super().__init__() 
     self.setWindowTitle('Main Window') 

app = QApplication([]) 
main_window = MainWindow() 
main_window.show()  
app.exec_() 