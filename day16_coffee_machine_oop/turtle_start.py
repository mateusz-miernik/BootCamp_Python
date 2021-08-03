"""
    DAY 16: First OOP, turtle module.
"""

from turtle import Turtle, Screen
from math import sqrt, pi


def draw_circle(obj: Turtle, size=1) -> None:
    obj.color("DeepSkyBlue", "DeepPink")
    radius = round(sqrt((360*size)/pi), 2)
    print(f"Radius of a circle is: {radius}")
    obj.begin_fill()
    for _ in range(360):
        obj.forward(size)
        obj.left(1)
    obj.end_fill()


def draw_square(obj: Turtle, size=10) -> None:
    obj.color("red", "yellow")
    obj.begin_fill()
    for _ in range(4):
        obj.forward(size)
        obj.left(90)
    obj.end_fill()


def draw_rectangle(obj: Turtle, side_a=20, side_b=10) -> None:
    obj.color("red", "blue")
    obj.begin_fill()
    for i in range(4):
        if i == 0 or i % 2 == 0:
            obj.forward(side_a)
        else:
            obj.forward(side_b)
        obj.left(90)
    obj.end_fill()


def draw_square_orbits(obj: Turtle, size=10, amount=8):
    radius = round(sqrt((4 * size*amount)/pi), 2)
    print(f"Radius of a circle with square orbits is: {radius}")
    for _ in range(amount):
        draw_square(obj, size)
        obj.pu()
        obj.forward(size*3)
        obj.left(360/amount)
        obj.pd()


def main() -> None:
    my_screen = Screen()
    my_screen.screensize(800, 640)
    matthew = Turtle()
    matthew.shape("turtle")
    matthew.speed(0)
    print(matthew)
    draw_circle(matthew)

    matthew.pu()
    matthew.right(90)
    matthew.forward(100)
    matthew.left(90)
    matthew.pd()

    draw_square_orbits(matthew, 5, 20)

    matthew.pu()
    matthew.right(90)
    matthew.forward(50)
    matthew.left(90)
    matthew.pd()
    draw_rectangle(matthew, 50, 20)
    my_screen.exitonclick()


if __name__ == "__main__":
    main()
