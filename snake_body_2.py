from random import choice

# canvas screen dimensions in px
C_DIMENSION = 400

CELL_SIZE = 20 # BOARD cell size
BOARD = [[(x, y) for x in range(0, C_DIMENSION+CELL_SIZE, CELL_SIZE)] for y in range(0, C_DIMENSION+CELL_SIZE, CELL_SIZE)] # game field where the snake is in moving

class SubElement:

    def __init__(self, dx, dy):
        self.dx, self.dy = dx, dy # warning, reverse meaning of direction

    def get_position(self):
        return self.dx, self.dy

class Snake:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = [SubElement(C_DIMENSION//CELL_SIZE//2, y) for y in range(11, 8, -1)]
        self.fruit = None
        self.x = 0
        self.y = 1

    def get_snake_position(self):
        'return list of all snake tuples demensions'
        return [x.get_position() for x in self.snake]

    def create_fruit(self):
        'the fruit object creation without snake position'
        snake_position = self.get_snake_position()

        while True:
            x = choice(range(0, C_DIMENSION//CELL_SIZE))
            y = choice(range(0, C_DIMENSION//CELL_SIZE))

            if (x, y) not in snake_position:
                break

        self.fruit = SubElement(x, y) # creating new fruit object in safety position in the game board
        

    def create_game_object(self, list_obj, color="gray"):
        'translate indexis to the BOARD demensions and drawing an object'
        for s in list_obj:
            x_coord, y_coord = s.get_position() # get coordination of the object
            self.canvas.create_rectangle(BOARD[x_coord][y_coord], BOARD[x_coord+1][y_coord+1], fill=color) # game_object to the screen


    def snake_move(self):
        x_coord, y_coord = self.snake[0].get_position()
        x_coord += self.x
        y_coord += self.y

        if self.fruit == None:
            self.create_fruit()
        
        self.snake.insert(0, SubElement(x_coord, y_coord))


        self.snake.pop()
        self.canvas.delete('all')
        self.create_game_object(self.snake)
        self.create_game_object((self.fruit), color='red')

        


        self.canvas.after(300, self.snake_move)

        # Snake move control Start
    def move_up(self, event=None):
        self.x = -1
        self.y = 0

    def move_down(self, event=None):
        self.x = 1
        self.y = 0

    def move_left(self, event=None):
        self.x = 0
        self.y = -1

    def move_right(self, event=None):
        self.x = 0
        self.y = 1
    # Snake move control Stop

    

if __name__ == "__main__":
    snake = Snake()
    print(snake.get_snake())
    
