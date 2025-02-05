from tkinter import *
# main window
window = Tk()
window.configure(bg="#73f094")
window.title("Snake Game")
window.iconbitmap("snake.ico")

# score label for actual state of score
score = Label(window, text="Score: 0", font=("Helvetica", 32, "bold"), bg="#73f094")
score.grid(row=0, column=1)

# canvas for snake area
canvas = Canvas(window, width=400, height=400, bg="white")
canvas.grid(row=1, column=1)

# Buttons control via mause
w = Button(window, text=" W ", command="", width=4).grid(row=2, column=1)
a = Button(window, text=" A ", command="", width=4).grid(row=3, column=0)
s = Button(window, text=" S ", command="", width=4).grid(row=3, column=1)
d = Button(window, text=" D ", command="", width=4).grid(row=3, column=2)

# snake function
def snake():
    canvas.create_rectangle(100, 100, 110, 110, fill="black")

# snake initialization
snake()


# main loop
window.mainloop()