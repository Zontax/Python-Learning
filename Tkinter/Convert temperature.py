import tkinter as tk


def fahrenheit_to_celsius():
    """Фаренгейт в градуси Цельсія"""
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


# Створення вікна
window = tk.Tk()
window.title("Температура F->C ")
window.resizable(width=False, height=False)
# window.iconbitmap("ico/pic.ico")  # іконка
# window.geometry(f"{wight}x{height}+{xw}+{yw}")
window.geometry("300x200+630+270")  # розмір та положення

# Створення рамки для введення значення по Фаренгейту через віджет
# однорядкового текстового поля разом з ярликом.
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Макет для рамки введення температури та ярлика з символом F
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Створення кнопки та лейбла
btn_convert = tk.Button(master=window,
                        text="\N{RIGHTWARDS BLACK ARROW}",
                        command=fahrenheit_to_celsius)  # кнопка зі стрілкою
lbl_result = tk.Label(master=window,
                      text="\N{DEGREE CELSIUS}")  # лейбл результату С

# Макет програми
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Запуск
window.mainloop()
