import turtle

def main():
    t = turtle.Turtle()
    turtle.title("Hello, there!")   # string that is shown in the titlebar of the turtle graphics window
    t.shape("turtle")
    t.color('gray', 'green') # pencolor, fillcolor

    # draw_pentagon(t)
    draw_star(t)

    # screen = turtle.Screen()
    # screen.exitonclick()
    turtle.exitonclick()    # Bind bye() method to mouse clicks on the Screen.

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