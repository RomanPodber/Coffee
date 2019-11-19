# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coffee.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 100, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 180, 291, 211))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 301, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 301, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Информация о сортах кофе</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Показать результат"))

class Coffee(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.res)

        self.coffee = ['Серрадо', 'Уила', 'Иргачефф', 'Бариста', 'Можиана', 'АА Маунт', 'Арабика']
        for i in self.coffee:
            self.comboBox.addItem(i)

    def res(self):
        self.listWidget.clear()
        self.characteristics = []
        self.characteristics.append('Название сорта | Прожарка | Состояние | Вкус | Цена за упаковку | Объем упаковки'
                                    '| Страна изготовитель')
        self.chose = self.comboBox.currentText()
        conn = sqlite3.connect('coffee.db')
        cur = conn.cursor()
        coffee = cur.execute(f"""SELECT name, quality, type, taste, cost, value FROM main WHERE name =
                             '{self.chose}'""").fetchall()
        country = cur.execute(f"""SELECT name FROM countries WHERE id = (SELECT country FROM main WHERE name
                                  = '{self.chose}')""")

        for i in coffee:
            box = []
            for k in i:
                box.append(str(k))
            for j in country:
                for m in j:
                    box.append(m)
            self.characteristics.append(' | '.join(box))

        for i in self.characteristics:
            self.listWidget.addItem(i)
        self.listWidget.show()

app = QApplication(sys.argv)
ex = Coffee()
ex.show()
sys.exit(app.exec_())
