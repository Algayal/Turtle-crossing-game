"""Main module creates the turtle crossing game"""
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# Creating am empty screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # turning animation off and using later update function


player = Player()
player.create_player()

# Listening to the keyboard and assigning the move player function to a key
screen.listen()
screen.onkey(fun=player.move_player, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)  # delay the execution(seconds)
    screen.update()

    car_manager.create_car()
    car_manager.move_car(car_manager.speed)

    # detecting collision between player and the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_game_text()

    # detecting if player reaches the end of a level
    if player.ycor() > 300:
        player.clear()
        player.create_player()
        car_manager.speed += 5
        car_manager.move_car(car_manager.speed)
        scoreboard.level += 1
        scoreboard.level_text()


screen.exitonclick()
