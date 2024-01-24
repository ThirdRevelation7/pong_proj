from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


def player_winner(player_side):
    floof = Turtle("turtle")
    floof.color("deep pink", "cyan")
    floof.goto(0, -10)
    floof.write(arg=f"{player_side} Player Wins!",
                align="center", font=("Courier", 30, "normal"))


def make_lines():
    lines = Turtle()
    lines.color("white")
    lines.hideturtle()
    lines.up()
    lines.goto(0, 280)
    lines.setheading(270)
    lines.width(2)
    for _ in range(10):
        lines.down()
        lines.fd(50)
        lines.up()
        lines.fd(50)


def pong():
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    make_lines()
    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    game_on = True
    while game_on:
        time.sleep(ball.ball_speed)
        print(ball.ball_speed)
        screen.update()
        ball.move()

        # Detects collision with the upper/lower wall and bounces off
        if ball.ycor() > 280 or ball.ycor() < -275:
            ball.bounce_y()

        # Detects collision with paddles and rebounds off
        if ball.xcor() > 320 and ball.distance(r_paddle) < 60 or ball.xcor() < -320 and ball.distance(l_paddle) < 60:
            ball.bounce_x()

        # Detects when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detects when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        # Detects a winner and ends game
        if scoreboard.l_score >= 3:
            game_on = False
            player_side = "Left"
            player_winner(player_side)
            screen.exitonclick()
        elif scoreboard.r_score >= 3:
            game_on = False
            player_side = "Right"
            player_winner(player_side)
            screen.exitonclick()


if screen.textinput("Would you like to play snake?", "Enter 'yes' or 'no': ") == "yes":
    pong()
else:
    screen.exitonclick()
