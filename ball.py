from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = .1

    def move(self):
        """Moves ball with slight increment to x and y axis"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverses direction of balls travel on the y_axis. When ball contacts ceiling/floor of box."""
        self.y_move *= - 1

    def bounce_x(self):
        """Reverses direction of balls travel on the x_axis. When ball contacts paddle."""
        self.x_move *= - 1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = .07
