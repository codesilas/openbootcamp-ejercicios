from email.policy import default
from faulthandler import disable
from tkinter import W, ttk
import tkinter

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

button_1 = tkinter.Radiobutton(window, )
button_2 = tkinter.Radiobutton(window, )
button_3 = tkinter.Radiobutton(window, )

button_1.grid(column=0, row=0, ipadx=5, ipady=5)
button_2.grid(column=0, row=1, ipadx=5, ipady=5)
button_3.grid(column=0, row=2, ipadx=5, ipady=5)

restart_button = tkinter.Button(window, text="Restart")
restart_button.grid(column=1, row=0)

window.tk.mainloop()