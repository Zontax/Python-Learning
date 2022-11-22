import pickle, sys
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def save_to_file():
    global start_date, calc_date, description
    data_to_save = {"start": start_date, "end": calc_date, "desc": description}
    file1 = open("config.txt", "wb")
    pickle.dump(data_to_save, file1)
    file1.close()


def read_from_file():
    global start_date, calc_date, description, now_date
    try:
        file1 = open("config.txt", "rb")
        data_to_load = pickle.load(file1)
        file1.close()
        start_date = data_to_load["start"]
        calc_date = data_to_load["end"]
        description = data_to_load["desc"]
        print('Сьогодні:', start_date.toString('dd-MM-yyyy'), 'Подія:', calc_date.toString('dd-MM-yyyy'), description)
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(description)
        delta_days_left = start_date.daysTo(now_date)  # пройшло днів
        delta_days_right = now_date.daysTo(calc_date)  # залишилось днів
        days_total = start_date.daysTo(calc_date)  # всього днів
        # print(delta_days_left, delta_days_right, days_total)
        procent = int(delta_days_left * 100 / days_total)
        form.progressBar.setProperty("value", procent)
        # print(procent, '%')
    except:
        print("Не могу прочитать файл конфигурации (Может его нет )))!)")


def on_click():
    global calc_date, description, start_date
    start_date = now_date
    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()
    save_to_file()
    print(start_date.toString('dd-MM-yyyy'), calc_date.toString('dd-MM-yyyy'), description)
    print("Збережено в config.txt")


def on_click_calendar():
    global start_date, calc_date
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    form.label_3.setText('До події залишилось: %s днів' % delta_days)


def on_dateedit_change():
    global start_date, calc_date
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
    form.label_3.setText('До події залишилось: %s днів' % delta_days)
    print(delta_days)


form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_change)

start_date = form.calendarWidget.selectedDate()
now_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
description = form.plainTextEdit.toPlainText()
read_from_file()

form.label.setText("Сьогодні: %s" % start_date.toString('dd-MM-yyyy'))
on_click_calendar()

app.exec_()
