import turtle

def main():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color('gray', 'green') # pencolor, fillcolor

    # draw_pentagon(t)
    draw_star(t)

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