import csv
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
import os
import customtkinter
import sys
import pdb

files=[]
names=[]

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle("Teacher Portal")
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowOpacity(0.95)

        self.F1 = QtWidgets.QFrame(self)
        self.F1.setGeometry(10, 10, 620, 120)
        self.F1.setStyleSheet("background-color: #aaa")

        self.F2 = QtWidgets.QFrame(self)
        self.F2.setGeometry(10, 140, 620, 330)
        self.F2.setStyleSheet("background-color: #ccc")

        self.add_button = QtWidgets.QPushButton("Add", self.F1)
        self.add_button.clicked.connect(self.add)
        self.add_button.setGeometry(30, 30, 100, 25)

        self.view_button = QtWidgets.QPushButton("View", self.F1)
        self.view_button.clicked.connect(self.evald)
        self.view_button.setGeometry(30, 70, 100, 25)

    def clear_frame(self):
        for widget in self.F2.children():
            widget.deleteLater()

    def evaluate(self, y):
        self.clear_frame()
        label = QtWidgets.QLabel("Weightage", self.F2)
        label.setStyleSheet("background-color: #aaa; color: black; font-size: 18px; font-weight: bold")
        label.setGeometry(30, 1, 100, 25)

        lab_reports = QtWidgets.QLabel("Lab Reports", self.F2)
        lab_reports.setGeometry(30, 55, 100, 25)
        entry = QtWidgets.QLineEdit(self.F2)
        entry.setGeometry(200, 54, 100, 25)

        lab_performance = QtWidgets.QLabel("Lab Performance", self.F2)
        lab_performance.setGeometry(30, 95, 100, 25)
        entry2 = QtWidgets.QLineEdit(self.F2)
        entry2.setGeometry(200, 95, 100, 25)

        midterm = QtWidgets.QLabel("Midterm", self.F2)
        midterm.setGeometry(30, 135, 100, 25)
        entry3 = QtWidgets.QLineEdit(self.F2)
        entry3.setGeometry(200, 135, 100, 25)

        final_term = QtWidgets.QLabel("Final term", self.F2)
        final_term.setGeometry(30, 175, 100, 25)
        entry4 = QtWidgets.QLineEdit(self.F2)
        entry4.setGeometry(200, 175, 100, 25)

        cea = QtWidgets.QLabel("Complex Engineering Activity", self.F2)
        cea.setGeometry(30, 210, 200, 25)
        entry5 = QtWidgets.QLineEdit(self.F2)
        entry5.setGeometry(200, 210, 100, 25)

        submit_button = QtWidgets.QPushButton("SUBMIT", self.F2)
        submit_button.clicked.connect(lambda: self.submit(y, int(entry.text()), int(entry2.text()), int(entry3.text()), int(entry4.text()), int(entry5.text())))
        submit_button.setGeometry(300, 260, 100, 25)

        reset_button = QtWidgets.QPushButton("RESET", self.F2)
        reset_button.clicked.connect(lambda: self.evaluate(y))
        reset_button.setGeometry(250, 260, 100, 25)

    def evald(self):
        self.clear_frame()
        global files
        global names
        if files:
            label = QtWidgets.QLabel("Select File", self.F2)
            label.setStyleSheet("background-color: #aaa")
            label.setGeometry(30, 30, 100, 25)

            clicked = QtCore.QStringListModel()
            clicked.setStringList(names)
            comboBox = QtWidgets.QComboBox(self.F2)
            comboBox.setModel(clicked)
            comboBox.setGeometry(30, 60, 100, 25)

            button = QtWidgets.QPushButton("Select", selfbutton.clicked.connect(lambda: self.evaluate(files[names.index(comboBox.currentText())])))
            button.setGeometry(30, 160, 100, 25)
        else:
            label = QtWidgets.QLabel("No Files Added", self.F2)
            label.setStyleSheet("background-color: #aaa; color: red")
            label.setGeometry(30, 60, 100, 25)

    def submit(self, clas, a1, a2, a3, a4, a5):
        self.clear_frame()

        clas["Performance total"] = (clas.iloc[:, 2:16].sum(axis=1) / 210) * a2
        clas["Lab Reports total"] = (clas.iloc[:, 16:30].sum(axis=1) / 210) * a1
        clas["Mid total"] = (clas.iloc[:, 30] / 55) * a3
        clas["Final total"] = (clas.iloc[:, 31] / 50) * a4
        clas["CEA total"] = (clas.iloc[:, 32] / 20) * a5
        clas["Grand total"] = (clas.iloc[:, 33:38].sum(axis=1))

        clas.loc[clas['Grand total'] >= 80, 'Grade'] = 'A'
        clas.loc[clas['Grand total'] >= 70, 'Grade'] = 'B'
        clas.loc[clas['Grand total'] >= 60, 'Grade'] = 'C'
        clas.loc[clas['Grand total'] >= 50, 'Grade'] = 'D'
        clas.loc[clas['Grand total'] < 50, 'Grade'] = 'F'

        label = QtWidgets.QLabel("Grades", self.F2)
        label.setStyleSheet("background-color: #aaa; color: black; font-size: 18px; font-weight: bold")
        label.setGeometry(30, 1, 100, 25)

        table = QtWidgets.QTableWidget(self.F2)
        table.setColumnCount(4)
        table.setRowCount(len(clas))
        table.setHorizontalHeaderLabels(["ID", "Name", "Total", "Grade"])
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for i in range(len(clas)):
            table.setItem(i, 1, QtWidgets.QTableWidgetItem(clas["Name"][i]))
            table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(round(clas["Grand total"][i], 2))))
            table.setItem(i, 3, QtWidgets.QTableWidgetItem(clas["Grade"][i]))
        table.setGeometry(30, 30, 600, 400)

        save_button = QtWidgets.QPushButton("SAVE", self.F2)
        save_button.clicked.connect(lambda: self.save(clas))
        save_button.setGeometry(300, 480, 100, 25)

    def save(self, clas):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "", "CSV (*.csv)")
        if file_name:
            clas.to_csv(file_name, index=False, encoding="utf-8")

    def upload(self):
        global files
        global names
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "CSV (*.csv)")
        if file_name:
            name = os.path.basename(file_name).split(".")[0]
            if name not in names:
                names.append(name)
                files.append(pd.read_csv(file_name))
                self.evald()
            else:
                messagebox = QtWidgets.QMessageBox(self)
                messagebox.setText("File already added")
                messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                messagebox.exec_()
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

