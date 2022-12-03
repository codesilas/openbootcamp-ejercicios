import tkinter
from tkinter import ttk

window = tkinter.Tk()

# grid usa una estructura de celdas, como un excel
# (0,0) (1,0) (2,0)
# (0,1) (1,1) (1,2)
# (0,2) (1,2) (2,2)
# (0,3) (1,3) (2,3)

# definiedno tamaño de ventana
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# insersion de label username
username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# entrada de datos username
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# insersion de label contraseña
password = ttk.Label(window, text="Contraseña:")
password.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# entrada de datos contraseña
password_entry= ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# boton
login_button = ttk.Button(window, text="login")
login_button.grid(column=1, row=2, sticky=tkinter.E)

window.mainloop()
