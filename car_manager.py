"""Module generates the moving obstacles"""
from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    """Creating the moving cars and defining the movement"""

    def __init__(self):
        self.all_cars = []
        self.speed = 10

    def create_car(self):
        """Creating the cars and moving them to the starting positions"""
        # We use the random choice so that each six times the loop runs a car gets created
        random_chance = randint(1, 6)

        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)

            new_car.goto(280, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self, speed):
        """Moving the cars"""
        for car in self.all_cars:
            car.forward(speed)
