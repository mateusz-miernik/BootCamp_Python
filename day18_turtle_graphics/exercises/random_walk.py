"""
    Title: Random walk designed with turtle module
"""

from turtle import Turtle, Screen
import pyautogui
import random as r

colors = ["magenta", "lime", "blue violet",
          "cyan", "gold", "firebrick1", "DarkSeaGreen"]


class RandomWalk:
    def __init__(self, turtle_obj, all_colors):
        self.turtle_obj = turtle_obj
        self.colors = all_colors
        self.directions_with_angles = {"NORTH": 90, "WEST": 180, "SOUTH": 270, "EAST": 360}

    def turtle_params(self, turtle_shape, pen_size, speed=0):
        self.turtle_obj.shape(turtle_shape)
        self.turtle_obj.pensize(pen_size)
        self.turtle_obj.speed(speed)

    def walk(self, distance=25):
        direction = r.choice(list(self.directions_with_angles.keys()))
        color = r.choice(self.colors)
        self.turtle_obj.color(color)
        angle = self.directions_with_angles[direction]
        print(f"Current direction is {direction}, angle={angle} degrees")
        angle_to_set = angle - self.turtle_obj.heading()
        self.turtle_obj.rt(angle_to_set)
        self.turtle_obj.fd(distance)


if __name__ == "__main__":
    mat = Turtle()
    screen = Screen()
    width, height = pyautogui.size()
    screen.screensize(width, height)
    random_walk = RandomWalk(mat, colors)
    random_walk.turtle_params("turtle", 10)

    while True:
        random_walk.walk()

    # screen.exitonclick()
