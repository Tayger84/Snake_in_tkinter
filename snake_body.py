"""
In building file for correct snake and its fruit behaviour.

"""


import random


class Snake:
    'class for snake body'
    def __init__(self, canvas):

        self.canvas = canvas

        self.cell_size = 10 # Snake body size

        self.snake_body = [0, 0, 0+self.cell_size, 0+self.cell_size] # x=200, y = 200 for the start position
        self.snake = canvas.create_rectangle(self.snake_body, fill="black")
        self.dx = 0
        self.dy = 0

    def move(self):
        self.canvas.move(self.snake, self.dx, self.dy)
        self.canvas.after(600, self.move)

# block for snake's control, event variables is necessary becasue key controls sends two parame0ters instead of one
    def move_up(self, event=None):
        self.dx = 0
        self.dy = -self.cell_size

    def move_down(self, event=None):
        self.dx = 0
        self.dy = self.cell_size

    def move_left(self, event=None):
        self.dx = -self.cell_size
        self.dy = 0

    def move_right(self, event=None):
        self.dx = self.cell_size
        self.dy = 0

       

class Fruit:
    """Fruits for showing: apple, banana, grape"""
    def __init__(self):
        self.apple = "apple.ico"
        self.banana = "banana.ico"
        self.grape = "grape.ico"
        