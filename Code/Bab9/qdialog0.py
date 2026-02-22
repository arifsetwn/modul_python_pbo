from PyQt6.QtWidgets import QApplication, QDialog 
  
class MyDialog(QDialog):      
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle('My Dialog') 
  
app = QApplication([]) 
dialog = MyDialog() 
dialog.show() 
app.exec()