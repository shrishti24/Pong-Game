from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

score = Score()

is_game_on = True

while is_game_on:

    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # if collision happens with upper and lower wall, the ball should bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_back_y()

    # if collision occurs with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_back_x()
        ball.move_speed *= 0.7

    # DETECT RIGHT PADDLE MISSES
    if ball.xcor() > 380:
        score.l_scores()
        ball.reset_position()

    # DETECT LIGHT PADDLE MISSES
    if ball.xcor() < -380:
        score.r_scores()
        ball.reset_position()

screen.exitonclick()
