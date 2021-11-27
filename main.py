import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.show_db)

    def show_db(self):
        try:
            self.con = sqlite3.connect('coffee.sqlite')
            cur = self.con.cursor()
            result = cur.execute(f"""SELECT * FROM cof""").fetchall()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(7)
            for el in result:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(el[0])))
                self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(el[1])))
                self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(el[2])))
                self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(el[3])))
                self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(el[4])))
                self.tableWidget.setItem(row_position, 5, QTableWidgetItem(str(el[5])))
                self.tableWidget.setItem(row_position, 6, QTableWidgetItem(str(el[6])))
        except sqlite3.OperationalError:
            self.label.setText('error operation')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
