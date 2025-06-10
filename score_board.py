from turtle import Turtle

class ScoreBoard(Turtle):
      def __init__(self):
          super().__init__()
          self.score= 0
          self.color("spring green")
          self.hideturtle()
          self.penup()
          self.setposition(0, 270)
          self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

      def updated_scoreboard(self):
          self.score += 1
          self.clear()
          self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
