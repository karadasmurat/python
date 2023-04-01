import random
import time
from turtle import Screen, Turtle

gamestate = "running"

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

FONT = ("Courier", 16, "normal")

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class Car:
    # Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen.
    def __init__(self) -> None:
        self.trtl = Turtle("square")
        self.trtl.shapesize(stretch_wid=1, stretch_len=2)
        self.trtl.color(random.choice(COLORS))
        self.trtl.penup()

        # random position along y axis (x is fixed, y is random)
        y_coord = random.randrange(-280, 280, 20)
        self.trtl.goto(290, y_coord)
        self.trtl.left(180)  # head west

    def move(self, dist: int):
        self.trtl.forward(dist)

    def xcor(self):
        return self.trtl.xcor()

    def clear_and_hide(self):
        self.trtl.clear()
        self.trtl.hideturtle()


class Player:
    def __init__(self):
        self.trtl = Turtle("square")
        self.trtl.color("white")
        # self.trtl.left(90)
        self.trtl.setheading(90)
        self.trtl.penup()
        self.trtl.goto(0, -280)

    def reset_position(self):
        self.trtl.penup()
        self.trtl.goto(0, -280)

    def up(self):
        self.trtl.forward(MOVE_DISTANCE)

    def collusion_ceiling(self):
        return self.trtl.ycor() > 270

    def collusion_car(self, car: Car):
        return self.trtl.distance(car.trtl) < 30


class CarManager:

    def __init__(self) -> None:
        self.cars = []
        self.state = "running"
        self.level = 0

    def create_car(self):
        self.cars.append(Car())

    def move_cars(self):
        if self.state == "running":
            for car in self.cars:
                car.move(STARTING_MOVE_DISTANCE + self.level * MOVE_INCREMENT)

    def collusion_cars_player(self, player: Player):
        collusion = False
        for car in self.cars:
            if car.trtl.distance(player.trtl.pos()) < 30:
                collusion = True

        return collusion

    def pause(self):
        self.state = "paused"

    def resume(self):
        self.state = "running"

    def manage_garbage(self):
        # destroy the turtle and garbage collect it
        for car in self.cars:
            if car.xcor() < -250:
                self.cars.remove(car)
                car.clear_and_hide()
                del car     # delete object to free up memory

    def get_active_car_count(self):
        return len(self.cars)

    def level_up(self):
        self.level += 1


class Scoreboard:
    def __init__(self) -> None:
        self.car_cnt = 0
        self.score = 0
        self.trtl = Turtle()
        self.trtl.color("white")
        self.trtl.penup()       # initstate, penup

        self.update_scoreboard()
        self.trtl.hideturtle()

    def update_scoreboard(self):
        self.trtl.clear()
        self.trtl.goto(-280, 280)
        self.trtl.write(f"Active Cars: {self.car_cnt}", align="left", font=FONT)

        self.trtl.goto(280, 280)
        self.trtl.write(f"Score: {self.score}", align="right", font=FONT)

    def increment_cars(self):
        self.car_cnt += 1

    def increment_score(self):
        self.score += 1

    def gameover(self):
        self.trtl.goto(0, 0)
        self.trtl.write(f"GAME OVER.", align="center", font=FONT)


def main():

    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Turtle Crossing Game")
    screen.bgcolor("black")
    screen.tracer(0)

    # Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
    player = Player()
    carmanager = CarManager()

    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(pause_game, "p")
    screen.onkey(resume_game, "r")
    # screen.onkey(carmanager.pause, "p")
    # screen.onkey(carmanager.resume, "r")

    loop_cnt = 0
    gameover = False
    while not gameover:
        if gamestate == "running":
            if loop_cnt % 5 == 0:
                loop_cnt = 0
                carmanager.create_car()
                scoreboard.car_cnt = carmanager.get_active_car_count()

            if carmanager.collusion_cars_player(player):
                gameover = True

            if player.collusion_ceiling():
                # gameover = True
                scoreboard.increment_score()
                player.reset_position()
                carmanager.level_up()

            carmanager.move_cars()
            carmanager.manage_garbage()
            scoreboard.update_scoreboard()

            loop_cnt += 1

        time.sleep(0.1)
        screen.update()

    scoreboard.gameover()

    screen.exitonclick()


def pause_game():
    print("PAUSE GAME")
    global gamestate
    gamestate = "paused"


def resume_game():
    global gamestate
    gamestate = "running"


if __name__ == "__main__":
    main()
