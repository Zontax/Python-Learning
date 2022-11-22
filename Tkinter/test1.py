import tkinter as tk
# якась дичина
window = tk.Tk()  # Вікно стандатного розміру

greeting = tk.Label(
    text="tk.Label Текст",
    fg="white",  # колір тексту
    bg="black",  # фон
    width=20,  # ширина
    height=2  # довжина
)  # Текст
greeting.pack()  # відображає віджети

entry = tk.Entry(width=20, )  # поле вводу
entry.pack()

button1 = tk.Button(
    text="tk.Button Нажми!",
    width=20,
    height=4,
    bg="blue",
    fg="yellow",
)
button1.pack()

text_box = tk.Text()
text_box.pack()

window.mainloop()  # Цикл для віджетів
