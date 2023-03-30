import random
import time
from turtle import Turtle, Screen

# a list of 3 tuples:
coordinates = [(0, 0), (-20, 0), (-40, 0)]
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SEGMENT_LENGTH = 20
FONT = ("Courier", 16, "normal")


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.initialize()
        self.head = self.segments[0]
        print("Constructed: ", [s.xcor() for s in self.segments])

    def initialize(self):
        for coord in coordinates:
            self.add_segment(coord)

    def add_segment(self, coord):
        t = Turtle(shape="square")
        tcolor = "white" if coord != (0, 0) else "DarkGreen"
        t.color(tcolor)
        t.penup()
        t.goto(coord)         # goto(x, y): two coordinates OR goto((x, y)): a pair (tuple) of coordinates
        self.segments.append(t)

    def extend(self):
        position_of_the_last = self.segments[-1].position()
        self.add_segment(position_of_the_last)

    def move(self):
        # from last to first, goto the position of the one before.
        # head goes one forward

        for index, value in reversed(list(enumerate(self.segments))):
            # print(index, value)
            if index == 0:
                # print("Moving the head")
                value.forward(20)
            else:
                # print("Moving segment: ", index)
                x = self.segments[index-1].xcor()
                y = self.segments[index-1].ycor()
                value.penup()
                value.goto((x, y))

    def up(self):
        # print("Going up!")
        self.head.setheading(90)  # North

    def down(self):
        # print("Going down!")
        self.head.setheading(270)  # South

    def left(self):
        # print("Going left!")
        self.head.setheading(180)  # West

    def right(self):
        # print("Going right!")
        self.head.setheading(0)   # East

    # annotate the type of a function’s return value -> expression
    # conventional getter
    # another option is to create an instance variable in the constructor !
    def get_head(self) -> Turtle:
        return self.segments[0]

    def collusion_with_walls(self):
        return self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290

    def collusion_with_tail(self):
        for s in self.segments:
            if s == self.head:
                continue
            elif self.head.distance(s) < 10:
                return True


class Food():
    def __init__(self) -> None:
        self.trtl = Turtle(shape="circle")
        self.trtl.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.trtl.color("red")
        self.relocate_food()

    def relocate_food(self):
        randx = random.randrange(-280, 281, SEGMENT_LENGTH)
        randy = random.randrange(-280, 281, SEGMENT_LENGTH)
        self.trtl.penup()
        self.trtl.goto(randx, randy)


class ScoreBoard:

    def __init__(self) -> None:
        self.score = 0
        self.trtl = Turtle()
        self.trtl.color("white")
        self.trtl.penup()
        self.trtl.goto(0, 260)
        self.update_scoreboard()
        self.trtl.hideturtle()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.trtl.clear()
        self.trtl.write(f"Score: {self.score}", align="center", font=FONT)

    def gameover(self):
        self.trtl.goto(0, 0)
        self.trtl.write(f"GAME OVER.", align="center", font=FONT)


def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Snake Game")
    screen.bgcolor("black")
    # turn off animation - perform TurtleScreen update manually (to make any updates visible).
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.update()  # update TurtleScreen (note that tracer is off)

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    gameover = False
    while not gameover:
        snake.move()

        # detect collusion with the food
        if snake.head.distance(food.trtl) < 10:
            # print("Collusion detected!")
            scoreboard.increment_score()
            food.relocate_food()
            snake.extend()

        # detect collusion with the walls or tail
        if snake.collusion_with_walls() or snake.collusion_with_tail():
            gameover = True

        screen.update()  # update TurtleScreen (note that tracer is off)
        time.sleep(0.1)

    scoreboard.gameover()

    screen.exitonclick()


def initialize():
    # a list of 3 tuples:
    coordinates = [(0, 0), (-20, 0), (-40, 0)]

    for c in coordinates:
        t = Turtle(shape="square")
        t.color("white")  # set both fillcolor and pencolor to given colorstring
        t.penup()
        t.goto(c)         # goto(x, y): two coordinates OR goto((x, y)): a pair (tuple) of coordinates


if __name__ == "__main__":
    main()
