import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Detect when turtle collides with the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


    #Detect if turtle reaches the end
    if player.ycor() > FINISH_LINE_Y:
        player.next_level()
        car_manager.next_level()
        scoreboard.increase_level()

    car_manager.create_car()
    car_manager.move_car()

screen.exitonclick()