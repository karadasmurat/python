"""
The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways.

The procedural interface provides functions which are derived from the methods of the classes Screen and Turtle.
They have the same names as the corresponding methods.
A screen object is automatically created whenever a function derived from a Screen method is called.

# in this example, turtle prefix is NOT an object. it is the module name, from "import turtle"
turtle.forward(50)  # function from procedural interface, default turtle.

star = turtle.Turtle()  # turtle instance creation
star.forward(50)  # turtle instance method

Turtle methods> Turtle motion> Move and draw
    forward()   Move the turtle forward by the specified distance, in the direction the turtle is headed.
    backward()  Move the turtle backward by distance, opposite to the direction the turtle is headed.
    right()     Turn turtle right by angle units. (clockwise)
    left()      Turn turtle left by angle units.
    speed()     Set the turtle's speed to an integer value in the range 0..10
    ...



"""
import random
from turtle import Turtle, Screen
from typing import List

FONT = ("Courier", 16, "normal")
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5


class Car:
    def __init__(self, position=(0, 0), wid=20, len=40) -> None:
        self.position = position
        self.width = wid
        self.length = len
        self.trtl = Turtle("square")
        self.trtl.color(random.choice(COLORS))  # choose a random color from the list
        self.trtl.shapesize(stretch_wid=wid/20, stretch_len=len/20)
        self.trtl.penup()
        self.trtl.goto(position)

    def move_up(self):
        print("UP")
        new_y = self.trtl.ycor() + MOVE_DISTANCE
        if new_y < 250:
            self.trtl.goto(self.trtl.xcor(), new_y)

    def move_down(self):
        self.trtl.penup()
        new_y = self.trtl.ycor() - MOVE_DISTANCE
        if new_y > -250:
            self.trtl.goto(self.trtl.xcor(), new_y)

    def move_right(self):
        print("RIGHT")
        new_x = self.trtl.xcor() + MOVE_DISTANCE
        if new_x < 250:
            self.trtl.goto(new_x, self.trtl.ycor())

    def move_left(self):
        new_x = self.trtl.xcor() - MOVE_DISTANCE
        if new_x < 250:
            self.trtl.goto(new_x, self.trtl.ycor())

    def X_West(self):
        return self.trtl.xcor() - (self.length/2)

    def X_East(self):
        return self.trtl.xcor() + (self.length/2)

    def Y_North(self):
        return self.trtl.ycor() + (self.width/2)

    def Y_South(self):
        return self.trtl.ycor() - (self.width/2)

    def is_collided_with(self, other):
        """
        West-damageable means west border of this is in between west-east borders of other
        sagi (veya solu), digerinin sagi ve solu arasinda ise x eksende hasar olasiligi var.
        yukarisi (veya asagisi), digerinin yukari ve asagisi arasinda ise y ekseninde hasar olasiligi var.
        """
        west_damageble = other.X_West() < self.X_West() and self.X_West() < other.X_East()
        east_damageble = other.X_West() < self.X_East() and self.X_West() < other.X_East()

        north_damageble = other.Y_South() < self.Y_North() and self.Y_North() < other.Y_North()
        south_damageble = other.Y_South() < self.Y_South() and self.Y_South() < other.Y_North()

        if (west_damageble):
            print("west_damageble")
        elif (east_damageble):
            print("east_damageble")

        if (north_damageble):
            print("north_damageble")
        elif (south_damageble):
            print("south_damageble")

        return (east_damageble or west_damageble) and (north_damageble or south_damageble)

    def __str__(self) -> str:
        return f"x1:{self.X_West()} , x2: {self.X_East()}"


def main():
    # t = Turtle(shape="turtle")  # ObjectOriented way
    # t.color('gray', 'green')    # pencolor, fillcolor

    # draw_pentagon(t)
    # draw_star(t)

    # screen.listen()
    # # screen.onkey(move, "m")

    # # how to pass a value to an event handler using lambda, and default value:
    # screen.onkey(lambda turtle=t: move(turtle), "m")

    # sketcher(t)
    # race()
    collusion_detect()


def write(msg, trtl):
    writer = trtl
    writer.color("white")
    writer.penup()
    writer.hideturtle()

    writer.clear()
    writer.goto(280, 280)
    writer.write(msg, align="right", font=FONT)


def collusion_detect():

    screen = Screen()  # # ObjectOriented way
    screen.title("Hello, there!")   # string that is shown in the titlebar of the turtle graphics window
    screen.bgcolor("black")
    screen.tracer(0)

    car2 = Car((100, 100), 40, 80)
    car1 = Car((0, 60), 20, 40)
    print(f"Check collusion: {car2.X_West()} < {car1.X_West()} < {car2.X_East()}")

    logger = Turtle()

    write(car2, logger)

    screen.listen()
    screen.onkey(car2.move_up, "Up")
    screen.onkey(car2.move_down, "Down")
    screen.onkey(car1.move_right, "Right")
    screen.onkey(car1.move_left, "Left")

    gameover = False
    while not gameover:
        if car1.is_collided_with(car2):
            # write("Collusion (X AXIS)", logger)
            print(f"Collusion !!!")

        screen.update()

    screen.exitonclick()


def sketcher(trtl: Turtle):

    screen = Screen()  # ObjectOriented way
    screen.title("Hello, there!")   # string that is shown in the titlebar of the turtle graphics window

    screen.listen()

    screen.onkey(lambda t=trtl: t.forward(10), "f")
    screen.onkey(lambda t=trtl: t.backward(10), "b")

    screen.onkey(lambda t=trtl: t.right(10), "r")
    screen.onkey(lambda t=trtl: t.left(10), "l")

    # how to pass a value to an event handler using lambda, and default value:
    screen.onkey(lambda t=trtl: clear(t), "c")

    screen.exitonclick()


def race():
    NUMBER_OF_TURTLES = 5
    WINDOW_HEIGHT = 400

    screen = Screen()  # ObjectOriented way
    screen.title("Turtle Race!")   # string that is shown in the titlebar of the turtle graphics window
    screen.setup(width=500, height=WINDOW_HEIGHT)
    # Center of the screen is (x=0, y=0)
    # If the width is 500, and height is 400, top right point is (x=250, y=200)

    # screen.textinput(title="Choose one", prompt="Which color will win?")

    racers = initialize(NUMBER_OF_TURTLES, WINDOW_HEIGHT)

    while not is_game_over(racers):
        move_one_step_in_random_order(racers)

    get_winner(racers)

    screen.exitonclick()


def initialize(turtle_cnt, window_height):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    dist_between_turtles = 400 / turtle_cnt
    y_offset = dist_between_turtles / 2
    top_y = window_height / 2 - y_offset
    turtles = []
    for i in range(turtle_cnt):
        t = Turtle(shape="turtle")
        t.color('gray', colors[i])  # pencolor, fillcolor
        t.penup()
        # line up vertically, on the left of the screen
        t.goto(x=-230, y=top_y - (i * dist_between_turtles))
        turtles.append(t)

    return turtles


def move_one_step_in_random_order(turtles: List[Turtle]):
    # Can every single turtle move at the same time?
    # If not, can they at least move in a random order?

    # turtles in the list would always be moved sequentially, so the first mover (turtles[0]) definitely would have an advantage.
    # for turtle in turtles:
    #     turtle.forward(random.randint(0, 10))

    # randomize the list first, then move sequentially
    random.shuffle(turtles)     # shuffle the list in place, and return None.
    for turtle in turtles:
        dist = random.randint(10, 11)
        print("Moving: ", turtle.color(), "forward by: ", dist)
        turtle.forward(dist)


def is_game_over(turtles: List[Turtle]):
    gameover = False
    for turtle in turtles:
        if turtle.xcor() >= 230:
            gameover = True

    return gameover


def get_winner(turtles: List[Turtle]):
    # can we have 2 or more winners?
    # yes, since all the turtles move in a single round, and the winner is check at the end of that round, there may be more than 1 winner.
    # (check this by making the distance moved a small range, so all moves almost the same)
    winners = []
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winners.append(turtle)

    if len(winners) == 0:
        print("No winner. Please try again.")
    elif len(winners) == 1:
        print("🌟 The winner is: ", winners[0].fillcolor())
    else:
        print("🌟🌟 We have ", len(winners), "winners: ", winners)
    return winners


def move(t: Turtle):
    '''A simple event handler'''
    t.forward(10)


def clear(t: Turtle):
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def draw_pentagon(t):
    for i in range(5):
        t.forward(100)
        t.right(72)     # turn right by angle units (clockwise)


def draw_star(t):
    ''' inside angles: 360 / 5 / 2 = 36 '''
    t.speed(1)
    t.right(108)
    t.forward(200)
    t.left(144)
    t.forward(200)
    t.left(144)
    t.forward(200)
    t.left(144)
    t.forward(200)
    t.left(144)
    t.forward(200)


if __name__ == "__main__":
    main()
