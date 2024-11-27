import turtle


def moveUp():
    x, y = pen.position()
    pen.setposition(x, y+5)

def moveDown():
    x, y = pen.position()
    pen.setposition(x, y-5)

def moveLeft():
    x, y = pen.position()
    print(x, y)
    pen.setposition(x-5, y)

def moveRight():
    x, y = pen.position()
    pen.setposition(x+5, y)

def penUp():
    global is_down
    if is_down:
        pen.up()
        is_down = False
    else:
        pen.down()
        is_down = True
    
is_down = True


window = turtle.Screen()
pen = turtle.Turtle()

window.onkeypress(moveUp, "Up")
window.onkeypress(moveDown, "Down")
window.onkeypress(moveLeft, "Left")
window.onkeypress(moveRight, "Right")
window.onkey(penUp, "space")

window.listen()
window.mainloop()