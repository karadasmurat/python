import time
from turtle import Turtle, Screen


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT = ("Courier", 88, "normal")


class Paddle:

    def __init__(self, position) -> None:
        self.trtl = Turtle("square")
        self.trtl.color("white")
        self.trtl.shapesize(stretch_wid=5, stretch_len=1)
        self.trtl.penup()
        self.trtl.goto(position)

    def up(self):
        # print("UP UP UP")
        self.trtl.penup()
        new_y = self.trtl.ycor() + 20
        if new_y < 250:
            self.trtl.goto(self.trtl.xcor(), new_y)

    def down(self):
        # print("DOWN DOWN DOWN")
        self.trtl.penup()
        new_y = self.trtl.ycor() - 20
        if new_y > -250:
            self.trtl.goto(self.trtl.xcor(), new_y)


class Ball:

    def __init__(self) -> None:
        self.trtl = Turtle("circle")
        self.trtl.color("white")
        # self.trtl.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed_x = 10  # the number of pixels that the ball moves to the right or left on each iteration of the game loop.
        self.speed_y = 10

    def reset(self):
        self.trtl.goto(0, 0)
        self.bounce_x_paddle()

    def move(self):
        '''update the position using speed_x and speed_y instance variables'''
        self.trtl.penup()
        self.trtl.goto(self.trtl.xcor() + self.speed_x, self.trtl.ycor() + self.speed_y)

    def collusion_ceil_or_floor(self):
        return self.trtl.ycor() > 280 or self.trtl.ycor() < -280

    def collusion_paddle(self, pdl: Paddle):
        return self.trtl.distance(pdl.trtl) < 50 and (self.trtl.xcor() > 340 or self.trtl.xcor() < -340)

    def has_p1_scored(self):
        return self.trtl.xcor() < -380

    def has_p2_scored(self):
        return self.trtl.xcor() > 380

    def bounce_y_ceil_or_floor(self):
        self.speed_y *= -1

    def bounce_x_paddle(self):
        self.speed_x *= -1


class ScoreBoard:

    def __init__(self) -> None:
        self.score_p1 = 0
        self.score_p2 = 0
        self.trtl = Turtle()
        self.trtl.color("white")
        self.trtl.penup()

        self.update_scoreboard()
        self.trtl.hideturtle()

    def increment_score_p1(self):
        self.score_p1 += 1
        self.update_scoreboard()

    def increment_score_p2(self):
        self.score_p2 += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.trtl.clear()
        self.trtl.goto(-180, 200)
        self.trtl.write(f"{self.score_p2}", align="center", font=FONT)
        self.trtl.goto(180, 200)
        self.trtl.write(f"{self.score_p1}", align="center", font=FONT)

    def gameover(self):
        self.trtl.goto(0, 0)
        self.trtl.write(f"GAME OVER.", align="center", font=FONT)


def main():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Pong Game")
    screen.bgcolor("black")
    # turn off animation - perform TurtleScreen update manually (to make any updates visible).
    screen.tracer(0)

    paddle_right = Paddle((350, 0))
    paddle_left = Paddle((-350, 0))

    ball = Ball()

    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(paddle_right.up, "Up")
    screen.onkey(paddle_right.down, "Down")
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")

    gameover = False
    while not gameover:
        ball.move()

        # detect collusion with the ceiling or floor
        if ball.collusion_ceil_or_floor():
            ball.bounce_y_ceil_or_floor()
        elif ball.collusion_paddle(paddle_right) or ball.collusion_paddle(paddle_left):
            ball.bounce_x_paddle()
        elif ball.has_p1_scored():
            scoreboard.increment_score_p1()
            ball.reset()
        elif ball.has_p2_scored():
            scoreboard.increment_score_p2()
            ball.reset()

        screen.update()
        time.sleep(0.05)

    screen.exitonclick()


if __name__ == "__main__":
    main()
