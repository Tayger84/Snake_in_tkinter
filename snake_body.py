import random

class Snake:
    'class for snake body'
    def __init__(self, canvas, window):
        self.window = window
        self.canvas = canvas
        self.snake = canvas.create_rectangle(100, 100, 110, 110, fill="black")
        self.dx = 10
        self.dy = 0

    def move(self):
        self.canvas.move(self.snake, self.dx, self.dy)
        self.canvas.after(800, self.move)

       

class Fruit:
    """Fruits for showing: apple, banana, grape"""
    def __init__(self):
        self.apple = "apple.ico"
        self.banana = "banana.ico"
        self.grape = "grape.ico"
        