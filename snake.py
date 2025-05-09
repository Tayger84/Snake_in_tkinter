from tkinter import Tk, Canvas, Button, Label, Frame
from snake_body import Snake, C_DIMENSION

def game():
    snake.snake_move()
    canvas.after(300, game)

# main window
window = Tk()
window.configure(bg="#73f094")
window.title("Snake Game")
window.focus_set()
window.iconbitmap("snake.ico")
window.resizable(False, False)  

# score label for actual state of score
score = Label(window, text="Score: 0 * High Score: 0", font=("Helvetica", 22, "bold"), bg="#73f094")
score.grid(row=0)

# canvas for snake area
canvas = Canvas(window, width=C_DIMENSION, height=C_DIMENSION, bg="white", highlightthickness=3, 
    highlightbackground='grey', relief="groove")
canvas.grid(row=1, padx=10, pady=10)

# Frame for Buttons
buttons_group = Frame(window, bg="#73e090")
buttons_group.grid(row=2, pady=10)

# snake initialization
snake = Snake(canvas, score)

game() # start of the Snake game


# Control of the snake
set_control = [
    (" ▲ ", "Up", 0, 0, 3, 5),
    (" ▼ ", "Down", 1, 1, None, 3),
    (" ◄ ", "Left", 1, 0, None, 3),
    (" ► ", "Right", 1, 2, None, 3)
]

for text, key, row, column, columnspan, pady in set_control:

    window.bind(f'<{key}>', lambda event, k=key: snake.moving(k)) # keyboard control
    Button(buttons_group, text=text, command=lambda k=key: snake.moving(k), width=4, font=("Helvetica", 15, "bold")).grid(row=row, column=column, columnspan=columnspan, pady=pady, padx=3) # Button control

# main loop
window.mainloop()