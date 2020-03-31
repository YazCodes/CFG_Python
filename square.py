import turtle

def square():
    side_lenght = 100
    angle = 90

    for side in range (4):
        turtle.forward(side_lenght)
        turtle.right(angle)

square()
