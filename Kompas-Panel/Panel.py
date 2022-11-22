from tkinter import *
import pythoncom
from win32com.client import Dispatch, gencache

#  Підключим API Компас
kompas6_constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
kompas6_constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

#  Підключим інтерфейси API5
kompas6_api5_module = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
kompas_object = kompas6_api5_module.KompasObject(
    Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(kompas6_api5_module.KompasObject.CLSID,
                                                             pythoncom.IID_IDispatch))

#  Читаєм данні з setting.txt
with open('setting.txt', 'r') as file:
    ks_command = file.read().splitlines()

#  Створюєм список команд
dict_ks_command = {}
for i in ks_command:
    n = i.split('=')
    dict_ks_command[n[1]] = n[0]

print(dict_ks_command)


def start(i):
    print(i)
    kompas_object.ksExecuteKompasCommand(dict_ks_command[i], False)


w = Tk()
w.title('Моя панель')  # Назва вікна
w.geometry("240x103+1238+147")  # Розмір вікна
w.resizable(True, False)  # Зміна розміру вікна
w.wm_attributes('-topmost', 1)  # По верх вікон
w.iconbitmap("img/pic.ico")  # Іконка вікна

i = 'Окружность с центром на объекте'
Button(text=i, command=lambda i=i: start(i)).grid(row=0, column=0)
i = 'Вспомогательная прямая'
Button(text=i, command=lambda i=i: start(i)).grid(row=1, column=0)
i = 'Эллипс по центру'
Button(text=i, command=lambda i=i: start(i)).grid(row=2, column=0)
i = 'Авторазмер'
Button(text=i, command=lambda i=i: start(i)).grid(row=3, column=0)

w.mainloop()
