from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def move_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def move_backwards():
    t.backward(10)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
