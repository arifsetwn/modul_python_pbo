from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QListWidget, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Contact Manager')

        # Membuat koneksi ke database SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("contacts.sqlite")

        # Membuka koneksi ke database
        if not self.db.open():
            print("Failed to open database")

        # Membuat tabel kontak jika belum ada
        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

        # Membuat widget daftar kontak
        self.listWidget = QListWidget()
        self.loadContacts()

        # Membuat tombol untuk operasi CRUD
        self.addButton = QPushButton("Add Contact")
        self.addButton.clicked.connect(self.addContact)
        self.deleteButton = QPushButton("Delete Contact")
        self.deleteButton.clicked.connect(self.deleteContact)

        # Membuat layout dan menambahkan widget
        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def loadContacts(self):
        # Mengambil semua kontak dari database
        query = QSqlQuery("SELECT * FROM contacts")
        self.listWidget.clear()
        while query.next():
            id = query.value(0)
            name = query.value(1)
            self.listWidget.addItem(f"{id}: {name}")

    def addContact(self):
        name, ok = QInputDialog.getText(self, "Add Contact", "Enter contact name:")
        if ok and name:
            query = QSqlQuery()
            query.prepare("INSERT INTO contacts (name) VALUES (:name)")
            query.bindValue(":name", name)
            if query.exec_():
                self.loadContacts()

    def deleteContact(self):
        currentRow = self.listWidget.currentRow()
        if currentRow > -1:
            id = self.listWidget.item(currentRow).text().split(":")[0]
            query = QSqlQuery()
            query.prepare("DELETE FROM contacts WHERE id = :id")
            query.bindValue(":id", id)
            if query.exec_():
                self.loadContacts()
        else:
            QMessageBox.warning(self, "Delete Contact", "Please select a contact to delete")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
