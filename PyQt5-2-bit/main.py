import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from colorama import Fore, init

Form, Window = uic.loadUiType("PyQt5-2-bit/interface.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
init()


def start():
    print("2-bit")
    inp1 = input('Ціле число у 2-кову систему: ')
    inp2 = inp1.isnumeric()  # Перевірка чи введено число True/False
    if inp2:  # True
        inp3 = bin(int(inp1))[2:]  # Перевод в 2-й код без "0b"
        print(Fore.GREEN, inp3, Fore.RESET)  # Вивід в 2-bit
    else:  # False
        print(Fore.RED, 'ERROR', Fore.RESET)  # Помилка коли False


def click_button():
    print("Оk")
    input('end: ')
    v = Form.sender().text()
    uic.lineEdit.setText(uic.lineEdit.text() + v)


form.button_1.clicked.connect(start)

app.exec_()
