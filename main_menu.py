from PyQt5 import QtCore, QtGui, QtWidgets
import sys
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
        self.Test.setStyleSheet("background-color: rgb(115, 164, 255);\n""")
        self.Test.setIconSize(QtCore.QSize(600, 20))
        self.Test.setAutoRepeatDelay(400)
        self.Test.setObjectName("Test")
        self.Dictionarybtm = QtWidgets.QPushButton(self.centralwidget)
        self.Dictionarybtm.setGeometry(QtCore.QRect(250, 390, 290, 170))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Dictionarybtm.setFont(font)
        self.Dictionarybtm.setStyleSheet("background-color: rgb(115, 164, 255);\n""")
        self.Dictionarybtm.setObjectName("Dictionary")
        Main_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main_menu)
        self.statusbar.setObjectName("statusbar")
        Main_menu.setStatusBar(self.statusbar)

        self.retranslateUi(Main_menu)
        QtCore.QMetaObject.connectSlotsByName(Main_menu)

    def __init__(self):
        self.Main_menu = QtWidgets.QMainWindow()
        self.setupUi(self.Main_menu)
        self.Dictionary = QtWidgets.QWidget()
        self.setupUidictionary(self.Dictionary)
        self.Dictionarybtm.clicked.connect(self.show_dictionary)

    def show_dictionary(self):
        self.Dictionary.show()
        self.Main_menu.close()

    def retranslateUi(self, Main_menu):
        _translate = QtCore.QCoreApplication.translate
        Main_menu.setWindowTitle(_translate("Main_menu", "Main_menu"))
        self.Training.setText(_translate("Main_menu", "Тренировка"))
        self.Test.setText(_translate("Main_menu", "Тест"))
        self.Dictionarybtm.setText(_translate("Main_menu", "Словарь"))

    def setupUidictionary(self, Dictionary):
        Dictionary.setObjectName("Dictionary")
        Dictionary.resize(787, 587)
        Dictionary.setStyleSheet("background-color: rgb(241, 203, 255);\n""")
        self.pushButton = QtWidgets.QPushButton(Dictionary)
        self.pushButton.setGeometry(QtCore.QRect(280, 500, 260, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(115, 164, 255);\n""")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dictionary)
        self.textBrowser.setGeometry(QtCore.QRect(15, 11, 761, 461))
        self.textBrowser.setStyleSheet("background-color: rgb(115, 164, 255);\n"
                                       "")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dictionary)
        QtCore.QMetaObject.connectSlotsByName(Dictionary)

    def retranslateUidictionary(self, Dictionary):
        _translate = QtCore.QCoreApplication.translate
        Dictionary.setWindowTitle(_translate("Dictionary", "Dictionary"))
        self.pushButton.setText(_translate("Dictionary", "Вернуться"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainwindow = Ui_Main_menu()

    mainwindow.Main_menu.show()
    sys.exit(app.exec_())
