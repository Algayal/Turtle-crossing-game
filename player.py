"""Module creates the player and defines control settings"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    """Creating the player"""

    def __init__(self):
        super().__init__()

    def create_player(self):
        """creating a turtle looking player and assigning it to a starting position"""
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player(self):
        """Moving a player a given distance"""
        self.forward(MOVE_DISTANCE)
