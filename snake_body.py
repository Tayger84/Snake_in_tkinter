import random
import time


class Snake:
    def __init__(self, canvas, window):
        self.window = window
        self.canvas = canvas
        self.snake = canvas.create_rectangle(100, 100, 110, 110, fill="black")

    def change_items(self):
        self.canvas.itemconfig(self.snake, fill="red")

    def snake_move(self, direction):
        self.canvas.move(self.snake, direction)
        
        

class Fruit:
    """Fruits for showing: apple, banana, grape"""
    def __init__(self):
        self.apple = "apple.ico"
        self.banana = "banana.ico"
        self.grape = "grape.ico"
        