import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename # Імпортуєм меню збереження та відкриття


def open_file():
    """Відкриває файл"""
    filepath = askopenfilename(
        filetypes=[("Текстові файли", "*.txt"), ("Python", "*.py"), ("Всі файли", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Блокнот - {filepath}")
 
def save_file():
    """Зберігає файл як новий"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстові файли", "*.txt"), ("Python", "*.py"), ("Всі файли", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Блокнот - {filepath}")

# Параметри вікна
window = tk.Tk()
window.title("Блокнот")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Кнопки і панелі
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Відкрити", command=open_file)
btn_save = tk.Button(fr_buttons, text="Зберегти як...", command=save_file)

# Положення кнопок
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Відображення GUI
window.mainloop()