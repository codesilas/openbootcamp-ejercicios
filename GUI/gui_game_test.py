import tkinter
import random

window = tkinter.Tk()

colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black']

for x in range(0, 10):
    color = random.randint(0, len(colors))
    color2 = random.randint(0, len(colors))
    
    label = tkinter.Label(window, text="etiqueta", bg=colors[color], fg=color[color])
    label.place(x=random.randint(0,100), y=random.randint(0,100))

window.mainloop()
