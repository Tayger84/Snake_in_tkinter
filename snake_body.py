"""
In building file for correct snake and its fruit behaviour.

"""
import random

cell_size = 20 # Snake body size
snake_color = "black"

class SubElement:
    'class for snake part'
    def __init__(self, dx, dy):
        self.x_coord = dx
        self.y_coord = dy

    def get_coords(self):
        'the method for coords reading'
        return [self.x_coord, self.y_coord, self.x_coord+cell_size, self.y_coord+cell_size]


class Fruit:
    
    def __init__(self):
        self.x = random.choice(range(0, 400, cell_size))
        self.y = random.choice(range(0, 400, cell_size))

    def get_coords(self):
        return self.x, self.y, self.x+cell_size, self.y+cell_size


class Snake:

    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = [SubElement(x_coord, 200) for x_coord in range(200, 200-3*cell_size, -cell_size)] # first snake initialization
        self.dx = cell_size # set first moving direction
        self.dy = 0
        self.create_snake() #first drawing snake
        self.fruit = None
    
    def create_snake(self):
        'method for snake drawing'
        for element in self.snake:
            self.canvas.create_rectangle(element.get_coords(), fill='gray', tags='snake')

    def move(self):
        'moving method for snake'
        x_coord, y_coord = self.snake[0].get_coords()[:2] # select snake head
        x_coord += self.dx
        y_coord += self.dy

        self.snake.insert(0, SubElement(x_coord,y_coord)) # new snake head creation
        self.snake.pop() # removing snake tail
        self.canvas.delete('snake') # delete snake_body 
        self.create_snake() # redrawing snake_body
        if self.fruit == None:
            self.fruit = self.canvas.create_rectangle(Fruit().get_coords(), fill="red", tags="fruit") # fruit generate
        
        self.canvas.after(300, self.move) # timer
    
    # Snake move control Start
    def move_up(self, event=None):
        self.dx = 0
        self.dy = -cell_size

    def move_down(self, event=None):
        self.dx = 0
        self.dy = cell_size

    def move_left(self, event=None):
        self.dx = -cell_size
        self.dy = 0

    def move_right(self, event=None):
        self.dx = cell_size
        self.dy = 0
    # Snake move control Stop


    