import tkinter as tk
from tkinter import ttk

# Crear una instancia de la clase Tk
window = tk.Tk()

ttk.Label(window, text="Mi programita").pack()

# Crear una lista de opciones
options = ["Opción 1", "Opción 2", "Opción 3"]

# Crear un ciclo for para generar un RadioButton para cada opción en la lista
for option in options:
    ttk.Radiobutton(window, text=option, value=option).pack()

window.mainloop()