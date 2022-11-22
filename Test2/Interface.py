from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("interface.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def click_button():
    print('Click')

form.pushButton.clicked.connect(click_button)

app.exec_()
