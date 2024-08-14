from turtle import Turtle, Screen

t = Turtle()


screen = Screen()
screen.listen()


def move_fd():
    t.fd(10)


def move_bd():
    t.bk(10)


def move_clock():
    t.right(5)


def move_counter():
    t.left(5)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bd)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="a", fun=move_counter)
screen.onkey(key="c", fun=clear)



screen.exitonclick()