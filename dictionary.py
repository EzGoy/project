from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dictionary(object):
    def __init__(self):
        self.pushButton = None
        self.textBrowser = None

    def setupUi(self, Dictionary):
        Dictionary.setObjectName("Dictionary")
        Dictionary.resize(787, 587)
        Dictionary.setStyleSheet("background-color: rgb(241, 203, 255);\n"
                                 "")
        self.pushButton = QtWidgets.QPushButton(Dictionary)
        self.pushButton.setGeometry(QtCore.QRect(280, 500, 260, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(115, 164, 255);\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dictionary)
        self.textBrowser.setGeometry(QtCore.QRect(15, 11, 761, 461))
        self.textBrowser.setStyleSheet("background-color: rgb(115, 164, 255);\n"
                                       "")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dictionary)
        QtCore.QMetaObject.connectSlotsByName(Dictionary)

    def retranslateUi(self, Dictionary):
        _translate = QtCore.QCoreApplication.translate
        Dictionary.setWindowTitle(_translate("Dictionary", "Dictionary"))
        self.pushButton.setText(_translate("Dictionary", "Вернуться"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dictionary = QtWidgets.QWidget()
    ui = Ui_Dictionary()
    ui.setupUi(Dictionary)
    Dictionary.show()
    sys.exit(app.exec_())
