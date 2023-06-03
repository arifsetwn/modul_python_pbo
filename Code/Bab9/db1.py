from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        # Membuat koneksi ke database SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database.sqlite")  # Database disimpan dalam file disk

        # Membuka koneksi ke database
        if not self.db.open():
            print("Failed to open database")

        # Membuat tabel dalam database
        query = QSqlQuery()
        query.exec_("CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT)")

        # Menambahkan data ke tabel
        query.exec_("INSERT INTO people (name) VALUES ('Setiawan Arif')")

        # Mengambil data dari tabel
        query.exec_("SELECT * FROM people")
        while query.next():
            print(query.value(1))

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
