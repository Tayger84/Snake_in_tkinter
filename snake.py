from tkinter import Tk, Canvas, Button, Label, Frame
from snake_body import Snake, Fruit

# main window
window = Tk()
window.configure(bg="#73f094")
window.title("Snake Game")
window.iconbitmap("snake.ico")
window.resizable(False, False)

# score label for actual state of score
score = Label(window, text="Score: 0", font=("Helvetica", 32, "bold"), bg="#73f094")
score.grid(row=0)

# canvas for snake area
canvas = Canvas(window, width=400, height=400, bg="white", highlightthickness=3, 
    highlightbackground='grey', relief="groove")
canvas.grid(row=1, padx=10, pady=10)

# Frame for Buttons
buttons_group = Frame(window, bg="#73e090")
buttons_group.grid(row=2, pady=10)

# snake initialization
snake = Snake(canvas, window)
#snake.snake_move(10, 0)

snake.move()

# Buttons control via mause
w = Button(buttons_group, text=" ▲ ", command=snake.move_up, width=4, font=("Helvetica", 15, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
a = Button(buttons_group, text=" ◄ ", command=snake.move_left, width=4, font=("Helvetica", 15, "bold")).grid(row=1, column=0, padx=3)
s = Button(buttons_group, text=" ▼ ", command=snake.move_down, width=4, font=("Helvetica", 15, "bold")).grid(row=1, column=1, padx=3)
d = Button(buttons_group, text=" ► ", command=snake.move_right, width=4, font=("Helvetica", 15, "bold")).grid(row=1, column=2, padx=3)







# main loop
window.mainloop()
