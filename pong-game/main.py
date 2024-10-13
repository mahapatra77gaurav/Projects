import time
import turtle
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 60 or ball.xcor() < -320 and ball.distance(l_paddle) < 60:
        ball.bounce_x()

    #Detect when R paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.increase_l_score()

    #Detect when L paddle misses
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.increase_r_score()

screen.exitonclick()