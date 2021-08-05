"""
    Title: Random walk designed with turtle module
"""

from turtle import Turtle, Screen
from random import choice
from ctypes import windll

colors = ["magenta", "lime", "blue violet",
          "cyan", "gold", "firebrick1", "DarkSeaGreen"]


class RandomWalk:
    def __init__(self, turtle_obj, all_colors, screen_width, screen_height):
        self.height = screen_height
        self.width = screen_width
        self.turtle_obj = turtle_obj
        self.colors = all_colors
        self.directions_with_angles = {"NORTH": 90, "WEST": 180, "SOUTH": 270, "EAST": 360}
        self.directions = list(self.directions_with_angles.keys())

    def _movement_control(self, distance):
        # print(f"Current position X: {self.turtle_obj.xcor()}, Y: {self.turtle_obj.ycor()}")
        up_max, down_max, left_max, right_max = self.height/2, -self.height/2, -self.width/2, self.width/2
        steps_after_exceeding_screen = 5

        if self.turtle_obj.xcor() > right_max:
            direction = "WEST"
        elif self.turtle_obj.xcor() < left_max:
            direction = "EAST"
        elif self.turtle_obj.ycor() > up_max:
            direction = "SOUTH"
        elif self.turtle_obj.ycor() < down_max:
            direction = "NORTH"
        else:
            direction = ""

        is_out_of_screen = True if direction else False
        direction = direction if direction else choice(self.directions)
        angle = self.directions_with_angles[direction]
        angle_to_set = angle - self.turtle_obj.heading()
        self.turtle_obj.rt(angle_to_set)

        if is_out_of_screen:
            self.turtle_obj.pu()
            for _ in range(steps_after_exceeding_screen):
                self.turtle_obj.fd(distance)
            self.turtle_obj.pd()
        else:
            self.turtle_obj.fd(distance)

    def set_turtle_params(self, turtle_shape, pen_size, speed=0):
        self.turtle_obj.shape(turtle_shape)
        self.turtle_obj.pensize(pen_size)
        self.turtle_obj.speed(speed)

    def walk(self, distance=25):
        color = choice(self.colors)
        self.turtle_obj.color(color)
        self._movement_control(distance)


if __name__ == "__main__":
    mat = Turtle()
    screen = Screen()
    user32 = windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen.setup(width, height, startx=0, starty=0)
    random_walk = RandomWalk(mat, colors, width, height)
    random_walk.set_turtle_params("turtle", 10)

    while True:
        random_walk.walk()

    # screen.exitonclick()
