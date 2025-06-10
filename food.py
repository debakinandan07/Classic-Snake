import random
from snake import Snake
from turtle import Turtle, Screen

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.position_x = (-280, 280)
        self.position_y = (-280, 280)
        # self.screen= Screen()
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("cyan")
        self.reappear()


    def reappear(self):
        random_x = random.randint(self.position_x[0], self.position_x[1])
        random_y = random.randint(self.position_y[0], self.position_y[1])
        self.setposition(random_x, random_y)



