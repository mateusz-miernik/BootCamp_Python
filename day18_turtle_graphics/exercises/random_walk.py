"""
    Title: Random walk designed with turtle module
"""

from turtle import Turtle, Screen
from random import choice
from ctypes import windll

colors = ["magenta", "lime", "blue violet",
          "cyan", "gold", "firebrick1", "DarkSeaGreen"]


class RandomWalk:
    def __init__(self, turtle_obj, all_colors):
        self.turtle_obj = turtle_obj
        self.colors = all_colors
        self.directions_with_angles = {"NORTH": 90, "WEST": 180, "SOUTH": 270, "EAST": 360}
        self.directions = list(self.directions_with_angles.keys())

    def set_turtle_params(self, turtle_shape, pen_size, speed=0):
        self.turtle_obj.shape(turtle_shape)
        self.turtle_obj.pensize(pen_size)
        self.turtle_obj.speed(speed)

    def walk(self, distance=25):
        direction = choice(self.directions)
        color = choice(self.colors)
        self.turtle_obj.color(color)
        angle = self.directions_with_angles[direction]
        # print(f"Current direction is {direction}, angle={angle} degrees")
        angle_to_set = angle - self.turtle_obj.heading()
        self.turtle_obj.rt(angle_to_set)
        self.turtle_obj.fd(distance)


if __name__ == "__main__":
    mat = Turtle()
    screen = Screen()
    user32 = windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen.setup(width, height, startx=0, starty=0)
    random_walk = RandomWalk(mat, colors)
    random_walk.set_turtle_params("turtle", 10)

    while True:
        random_walk.walk()

    # screen.exitonclick()
