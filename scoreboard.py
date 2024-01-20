"""Module for creating a scoreboard and updating it"""
from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """Creating the scoreboard and defining the end game text"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.level_text()

    def level_text(self):
        """Creating the Level text that appears on the window"""
        self.clear()
        self.write(f"Level:{self.level}", False, "center", FONT)
        self.hideturtle()

    def end_game_text(self):
        """ "Creating Game Over text"""
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
        self.hideturtle()
