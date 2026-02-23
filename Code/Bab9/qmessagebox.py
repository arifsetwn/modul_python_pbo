# Import necessary modules from PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

# Define a class named MainWindow that inherits from QMainWindow
class MainWindow(QMainWindow):
    # Define the constructor for the MainWindow class
    def __init__(self):
        # Call the constructor of the parent class (QMainWindow)
        super().__init__()
        # Create a QPushButton widget with the text "Show Message"
        button = QPushButton("Show Message")
        # Connect the clicked signal of the button to the show_message method
        button.clicked.connect(self.show_message)
        # Set the central widget of the main window to the button
        self.setCentralWidget(button)

    # Define a method to show a message box
    def show_message(self):
        # Show an information message box with the title "Hello!" and the message "This is a message."
        QMessageBox.information(self, "Hello!", "This is a message.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication([])
    # Create a MainWindow instance
    window = MainWindow()
    # Show the main window
    window.show()
    # Start the application event loop
    app.exec()
