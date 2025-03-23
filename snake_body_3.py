from random import choice

# canvas screen dimensions in px
C_DIMENSION = 400 # size of the canvas window
CELL_SIZE = 20 # BOARD cell size

direction = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}   # used to moving of the snake

class SubElement:
    'use to Snake part and fruit class'
    def __init__(self, dx, dy):
        self.dx, self.dy = dx, dy

    def get_position(self):
        return self.dx, self.dy

class Snake:
    'The main class for the Snake body'
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = [SubElement(C_DIMENSION//CELL_SIZE//2, y) for y in range(11, 8, -1)]
        self.fruit = self.create_fruit()
        self.score = 0
        self.x = 0
        self.y = 1

    def get_snake_position(self):
        'return list of all snake tuples demensions'
        return [x.get_position() for x in self.snake]
    
    def snake_head(self):
        x_coord, y_coord = self.snake[0].get_position()
        return x_coord + self.x, y_coord + self.y

    def create_fruit(self):
        'the fruit object creation out of the snake position'
        snake_position = self.get_snake_position()

        while True:
            x = choice(range(1, C_DIMENSION//CELL_SIZE-1))
            y = choice(range(1, C_DIMENSION//CELL_SIZE-1))

            if (x, y) not in snake_position:
                self.fruit = SubElement(x, y) # creating new fruit object in safety position in the game board
                return self.fruit

    def check_collision(self):
        x, y = self.snake_head()
        if x >= -1 and x <= CELL_SIZE and y >= -1 and y <= CELL_SIZE and self.get_snake_position()[0] not in self.get_snake_position()[1:]:
            return True
        else:
            return False
        
    def reset_snake(self):
        self.score = 0
        self.canvas.delete("all")
    
        
    def create_game_object(self, obj, color="gray"):
        'translate indexis to the BOARD demensions and drawing an object'
        #for s in list_obj:
        x_coord, y_coord = obj # get coordination of the object
        return self.canvas.create_oval(x_coord * CELL_SIZE, y_coord * CELL_SIZE, (x_coord + 1) * CELL_SIZE, (y_coord + 1) * CELL_SIZE, fill=color) # game_object to the screen
    
    def get_score(self):
        return self.score

    def moving(self, direct):
        'snake moving control method, based on the change main increase of x and y axes'
        if direct == "Up":
            if (self.x, self.y) != direction["Down"]:
                self.x, self.y = direction["Up"]
        if direct == "Down":
            if (self.x, self.y) != direction["Up"]:
                self.x, self.y = direction["Down"]
        if direct == "Left":
            if (self.x, self.y) != direction["Right"]:
                self.x, self.y = direction["Left"]
        if direct == "Right":
            if (self.x, self.y) != direction["Left"]:
                self.x, self.y = direction["Right"]


    def snake_move(self):
        
        self.canvas.delete("all")
        [self.create_game_object(part) for part in self.get_snake_position()] # snake drawing
        self.create_game_object((self.fruit.get_position()), color='red') # fruit drawing

        head = self.snake_head()
        self.snake.insert(0, SubElement(*head)) # new head in the snake body
        
        if head == self.fruit.get_position():
            self.create_fruit()
            self.score += 10
        else:
            self.snake.pop()

        if self.check_collision():
            self.canvas.after(200, self.snake_move)


        
# BOARD = [[(x, y) for x in range(0, C_DIMENSION+CELL_SIZE, CELL_SIZE)] for y in range(0, C_DIMENSION+CELL_SIZE, CELL_SIZE)] # game field where the snake is in moving