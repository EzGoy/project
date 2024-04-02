from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_menu(object):
    def setupUi(self, Main_menu):
        Main_menu.setObjectName("Main_menu")
        Main_menu.resize(787, 587)
        Main_menu.setStyleSheet("background-color: rgb(241, 203, 255);")
        self.centralwidget = QtWidgets.QWidget(Main_menu)
        self.centralwidget.setToolTip("")
        self.centralwidget.setToolTipDuration(0)
        self.centralwidget.setObjectName("centralwidget")
        self.Training = QtWidgets.QPushButton(self.centralwidget)
        self.Training.setGeometry(QtCore.QRect(250, 10, 290, 170))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Training.setFont(font)
        self.Training.setStyleSheet("background-color: rgb(115, 164, 255);")
        self.Training.setIconSize(QtCore.QSize(100, 200))
        self.Training.setObjectName("Training")
        self.Test = QtWidgets.QPushButton(self.centralwidget)
        self.Test.setGeometry(QtCore.QRect(250, 200, 290, 170))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Test.setFont(font)
        self.Test.setStyleSheet("background-color: rgb(115, 164, 255);\n"
                                "")
        self.Test.setIconSize(QtCore.QSize(600, 20))
        self.Test.setAutoRepeatDelay(400)
        self.Test.setObjectName("Test")
        self.Dictionary = QtWidgets.QPushButton(self.centralwidget)
        self.Dictionary.setGeometry(QtCore.QRect(250, 390, 290, 170))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Dictionary.setFont(font)
        self.Dictionary.setStyleSheet("background-color: rgb(115, 164, 255);\n"
                                      "")
        self.Dictionary.setObjectName("Dictionary")
        Main_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main_menu)
        self.statusbar.setObjectName("statusbar")
        Main_menu.setStatusBar(self.statusbar)

        self.retranslateUi(Main_menu)
        QtCore.QMetaObject.connectSlotsByName(Main_menu)

    def retranslateUi(self, Main_menu):
        _translate = QtCore.QCoreApplication.translate
        Main_menu.setWindowTitle(_translate("Main_menu", "Main_menu"))
        self.Training.setText(_translate("Main_menu", "Тренировка"))
        self.Test.setText(_translate("Main_menu", "Тест"))
        self.Dictionary.setText(_translate("Main_menu", "Словарь"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main_menu = QtWidgets.QMainWindow()
    ui = Ui_Main_menu()
    ui.setupUi(Main_menu)
    Main_menu.show()
    sys.exit(app.exec_())
