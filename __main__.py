import turtle, time, random, keyboard

class SnakeBlock(turtle.Turtle):
    xdirections = {0:0, 1:-30, 2:0, 3: 30}
    ydirections = {0:30, 1:0, 2:-30, 3: 0}
    def __init__(self, pos, direction, num):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1.4285714285714286,1.4285714285714286,1)
        self.pos = pos
        self.direction = direction
        self.goto(self.pos)
        self.num = num
        #         self.mini = turtle.Turtle()
        #         self.mini.color('white')
        #         self.mini.penup()
        #         self.mini.goto(self.pos)
        print(self)
    def next(self):
        self.pos = (self.pos[0]+self.xdirections[self.direction], self.pos[1]+self.ydirections[self.direction])
        self.goto(self.pos)
        ## print(f'{self.num} is at {self.pos}')
        #         self.mini.clear()
        #         self.mini.goto(self.pos)
        #         self.mini.write(self.pos)
    def __repr__(self):
        return f'SnakeBlock at {self.pos} facing {self.direction}'
class Snake:
    def __init__(self, length):
        self.length = length
        self.blocks = []
        self.turnplaces = []
        self.direction = 3
        for x in range(length):
            snake = SnakeBlock(((4-x)*30-420, 0), self.direction, x)
            self.blocks.append(snake)
        self.blocks.reverse()
    def left(self):
        print('left')
        new = {self.blocks[-1].pos: 1}
        self.turnplaces.append(new)
    def right(self):
        print('right')
        new = {self.blocks[-1].pos: 3}
        self.turnplaces.append(new)
    def up(self):
        print('up')
        new = {self.blocks[-1].pos: 0}
        self.turnplaces.append(new)
    def down(self):
        print('down')
        new = {self.blocks[-1].pos: 2}
        self.turnplaces.append(new)
    def checkforturns(self):
        keys = [next(iter(item.items()))[0] for item in self.turnplaces]
        values = [next(iter(item.items()))[1] for item in self.turnplaces]
        # ## print(keys, values)
        for snakeblock in self.blocks:
            if snakeblock.pos in keys:
                print(f'Turtle {list(reversed(snake.blocks)).index(snakeblock)} has turned')
                snakeblock.direction = values[keys.index(snakeblock.pos)]
                if self.blocks[snake.blocks.index(snakeblock)] == self.blocks[0]:
                    self.turnplaces.pop()

screen = turtle.Screen()
screen.setup(width=950, height=950, startx=300)
screen.colormode(255)
screen.bgcolor('blue')
screen.tracer(0)  ##

score = 0
score_ttl = turtle.Turtle()
score_ttl.penup()
score_ttl.goto(-430, 430)
score_ttl.color('white')
score_ttl.hideturtle()
apple = turtle.Turtle()
apple.shape('circle')
apple.shapesize(1.4285714285714286,1.4285714285714286,1)
apple.color('red')
apple.penup()
apple.goto(random.randint(-15,15)*30, random.randint(-15,15)*30)
    

def chomp():
    global score, snake
    score += 1
    apple.goto(random.randint(-15,15)*30, random.randint(-15,15)*30)
    pos = [snake.pos for snake in snake.blocks]
    while apple.pos in pos:
        apple.goto(random.randint(-15,15)*30, random.randint(-15,15)*30)
    newpos = list(snake.blocks[0].pos)
    if snake.blocks[0].direction == 0: newpos[1]+=30
    elif snake.blocks[0].direction == 1: newpos[0]-=30
    elif snake.blocks[0].direction == 2: newpos[1]-=30
    elif snake.blocks[0].direction == 3: newpos[0]+=30
    ## print(snake.blocks[0].direction)
    newblock = SnakeBlock(tuple(newpos),snake.blocks[0].direction,len(snake.blocks))
    snake.blocks.insert(0, newblock)
    screen.update()  ##
def is_dead():
    global snake
    headx = snake.blocks[-1].pos[0]
    heady = snake.blocks[-1].pos[1]
    if headx < -450 or headx > 450:
        return True
    elif heady < -450 or heady > 450:
        return True
    for snakeblock in snake.blocks[:-1]:
        if snakeblock.distance(snake.blocks[-1]) < 5:
            return True
    return False
def die():
    screen.bgcolor((0,0,110))
    death = turtle.Turtle()
    death.hideturtle()
    death.penup(); death.goto((-320, -50)); death.color('white'); death.write('Game Over', font=("Arial", 96, "normal"))
    apple.color(97,0,0)
    score_ttl.clear()
    score_ttl.penup(); score_ttl.goto(-100, -80); score_ttl.write(f'Score: {score}', font=("Arial", 36, "normal"))
    screen.update()
    time.sleep(3)
    raise SystemExit

snake = Snake(4)
screen.update()  ##
keyboard.add_hotkey('up', snake.up)
keyboard.add_hotkey('left', snake.left)
keyboard.add_hotkey('down', snake.down)
keyboard.add_hotkey('right', snake.right)
# with keyboard.Listener(on_press=report_turn) as listener:
#         listener.join()

while True:
    snake.checkforturns()
    [snakeblock.next() for snakeblock in snake.blocks]
    screen.update()  ##
    # time.sleep(0.1)
    if is_dead():
        break
    if snake.blocks[-1].pos == apple.pos():
        chomp()
    score_ttl.clear()
    score_ttl.write(score, font=("Arial", 24, "normal"))
    screen.update()
    time.sleep(1)
    
die()

