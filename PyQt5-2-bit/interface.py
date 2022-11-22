from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 170)
        MainWindow.setMinimumSize(QtCore.QSize(435, 170))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 170))
        MainWindow.setSizeIncrement(QtCore.QSize(435, 170))
        MainWindow.setBaseSize(QtCore.QSize(435, 170))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setMinimumSize(QtCore.QSize(430, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_1.setFont(font)
        self.label_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.button_1.setFont(font)
        self.button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_1.setAutoFillBackground(False)
        self.button_1.setObjectName("button_1")
        self.verticalLayout.addWidget(self.button_1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(430, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2-bit Число у двійковий код"))
        self.label_1.setText(_translate("MainWindow", "Введіть ціле десяткове число"))
        self.button_1.setText(_translate("MainWindow", "Oк"))
        self.label_2.setText(_translate("MainWindow", "Результат:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
