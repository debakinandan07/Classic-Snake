# import random
import time
from turtle import Turtle

class Snake:

    def __init__(self):
        self.all_squares = []
        self.STARTING_POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head= self.all_squares[0]


    def create_snake(self):
        """creating a 3-boxed snake at the start of the match"""

        for position in self.STARTING_POSITIONS:
            self.create_snake_segment(position)
        # self.all_squares[0].setposition
        # self.all_squares[1].setposition
        # self.all_squares[2].setposition


    def create_snake_segment(self, position):
        """creating a basic structure for snake"""

        new_square = Turtle("square")
        new_square.color("aquamarine")
        new_square.penup()
        new_square.speed(0)
        new_square.setposition(position)
        self.all_squares.append(new_square)


    def new_snake_body(self):
        """creating a new snake body after eating the food"""

        self.create_snake_segment(self.all_squares[-1].position())
        # for i in range(len(self.all_squares)-1, 0, -1):
        #    new_x= self.all_squares[i-1].xcor()
        #    new_y= self.all_squares[i-1].ycor()
        #    if self.head.heading() == 0:
        #        self.all_squares[i].setposition(new_x - 20, new_y)
        #
        #    elif self.head.heading() == 180:
        #        self.all_squares[i].setposition(new_x + 20, new_y)
        #
        #    elif self.head.heading() == 90:
        #        self.all_squares[i].setposition(new_x, new_y - 20)
        #
        #    elif self.head.heading() == 270:
        #        self.all_squares[i].setposition(new_x, new_y + 20)




    def follow_consistently(self):
        """movement of the snake"""

        for i in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[i - 1].xcor()
            new_y = self.all_squares[i - 1].ycor()
            self.all_squares[i].goto(new_x, new_y)
        self.head.forward(10)
        if self.head.xcor() > 300 or self.head.xcor() < -300:
            time.sleep(0.1)
            self.head.setx(-self.head.xcor())
        if self.head.ycor() > 300 or self.head.ycor() < -300:
            time.sleep(0.1)
            self.head.sety(-self.head.ycor())



    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    # def run(self):
    #     self.screen.mainloop()