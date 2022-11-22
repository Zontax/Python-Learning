import random
import time
from colorama import Fore, init
from tkinter import *

init()  # запуск колорами


def ochko():
    koloda36 = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4  # колода карт
    random.shuffle(koloda36)  # мішає карти
    print(Fore.YELLOW + 'Зіграєм в 21 очко?')
    ochko = 0  # очки
    while True:  # основний цикл
        print(Fore.GREEN)
        vubor = input('Будете брати карту? Yes/No (y/n)\n')  # ввід відповіді
        if 'y' in vubor or 'Y' in vubor or 'н' in vubor or 'Н' in vubor or 'Yes' in vubor or 'yes' in vubor or 'YES' in vubor:
            now = koloda36.pop(
            )  # pop видаляє елемент зі списку і виводить його
            print(Fore.RESET + 'Вам попалась карта %d' % now)
            ochko += now
            if ochko > 21:
                print('Ви проиграли! У вас %d' % ochko)
                break
            elif ochko == 21:
                print('Ви набрали 21 очко!')
                break
            else:
                print('Зараз у вас %d' % ochko)
        elif 'n' in vubor or 'N' in vubor or 'т' in vubor or 'Т' in vubor or 'No' in vubor or 'no' in vubor or 'NO' in vubor:
            print('Зараз у вас %d і ви закінчили гру' % ochko)
            break
        else:
            break

    print(Fore.YELLOW)
    print('Кінець гри!')
    time.sleep(0.7)
    input("\nНажміть ENTER щоб вийти ->")
    pass


def hul():
    n = 100
    while n > 0:
        n -= 7
        time.sleep(0.1)
        print(n, '- 7')
    print('Я, Programist...')
    pass


def btn(txt):
    print(txt)
    pass


window = Tk()  # створення вікна
window.title("Програма")
# window.geometry(f"{wight}x{height}+{xw}+{yw}")
window.geometry("600x350+525+150")
window.resizable(False, False)  # зміна розміру (х,у)
# window.iconbitmap("ico/pic.ico")  # іконка

txt = 'Гуль'
Button(text=txt, command=lambda txt=txt: hul()).grid(row=0, column=0)
txt = 'Очко'
Button(text=txt, command=lambda txt=txt: ochko()).grid(row=0, column=1)
txt = 'Кнопка'
Button(text=txt, command=lambda txt='Ми незалежні!': btn(txt)).grid(row=0,
                                                                    column=2)
window.mainloop()  # цикл вікна
