from PyQt5 import QtCore, QtGui, QtWidgets
def dron_square():
    up(50)
    down(100)
    up(100)
    down(100)
    up(100)
    down(100)
    up(100)
    down(100)
    up(100)
    down(100)
    up(50)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 120, 91, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 51))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setStyleSheet("background-color: rgb(17, 180, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addfunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "прога"))
        self.checkBox.setText(_translate("MainWindow", "по вертикали"))
        self.checkBox_2.setText(_translate("MainWindow", "по горизонтали"))
        self.checkBox_3.setText(_translate("MainWindow", "по квадрату"))
        self.label.setText(_translate("MainWindow", "выберите упражнения"))
        self.pushButton.setText(_translate("MainWindow", "взлёт"))
        self.pushButton_2.setText(_translate("MainWindow", "посадка"))
    def addfunctions(self):
        self.pushButton.clicked.connect(lambda:self.vzlet())
        self.pushButton.clicked.connect(lambda: self.posadka())
    def vzlet(self):
        #start()
        #takeoff()
        #up(100)
        if self.checkBox.isChecked():
            pass
            #left(50)
            #right(50)
            #left(50)
            #right(50)
            #left(50)
            #right(50)
            #left(50)
            #right(50)
            #left(50)
            #right(50)
        if self.checkBox_2.isChecked():
            dron_square()
            
        if self.checkBox_3.isChecked():
            pass
            #up(50)
            #right(50)
            #down(50)
            #left(50)
            #up(50)
            #right(50)
            #down(50)
            #left(50)
            #up(50)
            #right(50)
            #down(50)
            #left(50)
            #up(50)
            #right(50)
            #down(50)
            #left(50)
            #up(50)
            #right(50)
            #down(50)
            #left(50)
        land()
    def posadka(self):
        pass
        #land()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
