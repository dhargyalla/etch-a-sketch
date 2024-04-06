from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(270)

def clockwise():
    tim.right(270)

def clear_drawings():
    tim.clear()

screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear_drawings)

screen.exitonclick()

