"""
    Title: Random walk designed with turtle module
"""

from turtle import Turtle, Screen
from random import choice
from ctypes import windll

colors = ["magenta", "lime", "blue violet",
          "cyan", "gold", "firebrick1", "DarkSeaGreen"]


class RandomWalk:
    def __init__(self, turtle_obj: Turtle, all_colors: list, screen_width: int, screen_height: int):
        self.height = screen_height
        self.width = screen_width
        self.turtle_obj = turtle_obj
        self.colors = all_colors
        self.directions_with_angles = {"NORTH": 90, "WEST": 180, "SOUTH": 270, "EAST": 360}
        self.directions = list(self.directions_with_angles.keys())
        self.steps_after_exceeding_screen = 5
        self.up_max, self.down_max, self.left_max, self.right_max = \
            self.height/2, -self.height/2, -self.width/2, self.width/2

    def _movement_control(self, distance: int) -> None:
        # print(f"Current position X: {self.turtle_obj.xcor()}, Y: {self.turtle_obj.ycor()}")

        if self.turtle_obj.xcor() > self.right_max:
            direction = "WEST"
        elif self.turtle_obj.xcor() < self.left_max:
            direction = "EAST"
        elif self.turtle_obj.ycor() > self.up_max:
            direction = "SOUTH"
        elif self.turtle_obj.ycor() < self.down_max:
            direction = "NORTH"
        else:
            direction = ""

        is_out_of_screen = True if direction else False
        direction = direction if direction else choice(self.directions)
        angle = self.directions_with_angles[direction]
        self.turtle_obj.setheading(angle)

        if is_out_of_screen:
            self.turtle_obj.penup()
            self.turtle_obj.forward(distance * self.steps_after_exceeding_screen)
            self.turtle_obj.pendown()
        else:
            self.turtle_obj.forward(distance)

    def _set_random_color(self):
        color = choice(self.colors)
        self.turtle_obj.color(color)

    def set_turtle_params(self, turtle_shape: str, pen_size: int, speed=0) -> None:
        self.turtle_obj.shape(turtle_shape)
        self.turtle_obj.pensize(pen_size)
        self.turtle_obj.speed(speed)

    def walk(self, distance=25) -> None:
        self._set_random_color()
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
