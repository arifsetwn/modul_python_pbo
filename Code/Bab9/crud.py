from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        # Membuat koneksi ke database SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database.sqlite")

        # Membuka koneksi ke database
        if not self.db.open():
            print("Failed to open database")

        # Membuat tabel dalam database (Create)
        query = QSqlQuery()
        query.exec("CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT)")

        # Menambahkan data ke tabel (Create)
        query.exec("INSERT INTO people (name) VALUES ('Setiawan Arif')")

        # Mengambil data dari tabel (Read)
        query.exec("SELECT * FROM people")
        while query.next():
            for i in range(2): #range(2) karena terdapat 2 kolom dalam database
                print(query.value(i))

        # Memperbarui data dalam tabel (Update)
        query.exec("UPDATE people SET name = 'Jane Doe' WHERE id = 1")

        # Menghapus data dari tabel (Delete)
        query.exec("DELETE FROM people WHERE id = 1")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
