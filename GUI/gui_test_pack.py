import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text=f"hola", bg="black", fg="gray")
label_saludo.pack(ipadx=50, ipady=50, fill="x")

label_adios = tkinter.Label(window, text="adios", bg="black", fg="yellow")
label_adios.pack(ipadx=50, ipady=50, fill="x")

window.mainloop()
