import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)

pen = turtle.Turtle()
pen.speed(0)

drawing = False

def start_drawing(x, y):
    global drawing
    drawing = True
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def stop_drawing(x, y):
    global drawing
    drawing = False
    pen.penup()

def move_mouse(x, y):
    if drawing:
        pen.goto(x, y)

screen.onscreenclick(start_drawing, 1)
screen.getcanvas().bind('<B1-Motion>', lambda e: move_mouse(e.x - 400, 300 - e.y))

screen.mainloop()