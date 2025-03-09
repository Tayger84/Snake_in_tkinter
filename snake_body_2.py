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
    

class Fruit:
    
    def __init__(self):
            self.x = choice(range(0, C_DIMENSION//CELL_SIZE))
            self.y = choice(range(0, C_DIMENSION//CELL_SIZE))

    def get_fruit(self, snake):
        
    

class Snake:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = [SubElement(C_HIGHT//CELL_SIZE//2, y) for y in range(11, 8, -1)]
        self.fruit = None
        self.x = 0
        self.y = 1
        self.create_game_object(self.snake, 'snake')
        # self.create_game_object(self.fruit, 'fruit', 'red')


    def create_game_object(self, list_obj, tag, color="gray"):
        'this method is useful for a game object drawing to the BOARD'
        for s in list_obj:
            x_coord, y_coord = s.get_position() # get coordination of the object
            self.canvas.create_rectangle(BOARD[x_coord][y_coord], BOARD[x_coord+1][y_coord+1], fill=color, tags=tag) # game_object to the screen


    def snake_move(self):
        x_coord, y_coord = self.snake[0].get_position()
        x_coord += self.x
        y_coord += self.y
        if self.fruit == None:
            self.fruit = Fruit().get_fruit(self.snake)

        self.snake.insert(0, SubElement(x_coord, y_coord))


        self.snake.pop()
        self.canvas.delete('snake')
        self.create_game_object(self.snake, 'snake')
        


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
    
