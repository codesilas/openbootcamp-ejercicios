import tkinter
from tkinter import ttk

# Crear una lista de opciones
options = ["Opción 1", "Opción 2", "Opción 3"]

# Crear una instancia de la clase Tk
window = tkinter.Tk()

# Crear una variable que se usará para almacenar la opción seleccionada
selected_option = ""

# Crear un ciclo for para generar un RadioButton para cada opción en la lista
for option in options:
    ttk.Radiobutton(window, text=option, variable=selected_option, value=option).pack()

# Crear un botón de reinicio para dejar todo como al principio
ttk.Button(window, text="Reiniciar", command=lambda: selected_option.replace().pack())

# Mostr "" seleccionada en una etiqueta
ttk.Label(window, textvariable=selected_option).pack()


window.mainloop()