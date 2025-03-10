from tkinter import Tk, Canvas, Button, Label, Frame
from snake_body_2 import Snake, C_DIMENSION


# main window
window = Tk()
window.configure(bg="#73f094")
window.title("Snake Game")
window.focus_set()
window.iconbitmap("snake.ico")
window.resizable(False, False)  

# score label for actual state of score
score = Label(window, text="Score: 0", font=("Helvetica", 32, "bold"), bg="#73f094")
score.grid(row=0)

# canvas for snake area
canvas = Canvas(window, width=C_DIMENSION, height=C_DIMENSION, bg="white", highlightthickness=3, 
    highlightbackground='grey', relief="groove")
canvas.grid(row=1, padx=10, pady=10)

# Frame for Buttons
buttons_group = Frame(window, bg="#73e090")
buttons_group.grid(row=2, pady=10)

# snake initialization
snake = Snake(canvas)
snake.snake_move()
#snake.snake_move(10, 0)
#
#snake.move()

# Buttons control via mause
Button(buttons_group, text=" ▲ ", command=snake.move_up, width=4, font=("Helvetica", 15, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
Button(buttons_group, text=" ◄ ", command=snake.move_left, width=4, font=("Helvetica", 15, "bold")).grid(row=1, column=0, padx=3)
Button(buttons_group, text=" ▼ ", command=snake.move_down, width=4, font=("Helvetica", 15, "bold")).grid(row=1, column=1, padx=3)
Button(buttons_group, text=" ► ", command=snake.move_right, width=4, font=("Helvetica", 15, "bold")).grid(row=1, column=2, padx=3)

# Control via keyboard
window.bind("<Up>",  snake.move_up, None)
window.bind("<Down>", snake.move_down, None)
window.bind("<Left>", snake.move_left, None)
window.bind("<Right>", snake.move_right, None)





# main loop
window.mainloop()
