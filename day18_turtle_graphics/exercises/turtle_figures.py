from turtle import Turtle, Screen
import random as r

colors = ["magenta", "lime", "blue violet", "cyan", "gold", "firebrick1", "DarkSeaGreen"]


def draw_figure(obj: Turtle, number_of_sides=3, size=100):
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        obj.fd(size)
        obj.rt(angle)


def draw_dashed_line(obj: Turtle, segment_length=10, number_of_segments=10) -> None:
    for _ in range(number_of_segments):
        obj.fd(segment_length)
        obj.up()
        obj.fd(segment_length)
        obj.down()


tim = Turtle()
tim.shape("turtle")
tim.color("DeepSkyBlue")

for num in range(3, 11):
    tim.color(r.choice(colors))
    draw_figure(tim, num)

screen = Screen()
screen.exitonclick()
