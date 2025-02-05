from tkinter import *

canvas = Canvas(width=400, height=400)
canvas.pack()


def snake():
    canvas.create_rectangle(100, 100, 110, 110, fill="black")

snake()

mainloop()