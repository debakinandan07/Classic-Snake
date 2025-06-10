from turtle import Turtle
from score_board import ScoreBoard

class GameOver(Turtle):
     def __init__(self):
         super().__init__()
         self.score= ScoreBoard()
         self.color("red")
         self.hideturtle()
         self.penup()
         self.score.clear()
         self.write(arg=f"GAME OVER!", align="center", font=("Arial", 54, "normal"))
