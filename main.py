import time
import snake
from turtle import Screen
from food import Food
from score_board import ScoreBoard
from is_game_on import GameOver

game_on= True
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
food= Food()
snake= snake.Snake()
score= ScoreBoard()


screen.listen()
screen.onkeypress(snake.turn_right, "Right")
screen.onkeypress(snake.turn_up, "Up")
screen.onkeypress(snake.turn_left, "Left")
screen.onkeypress(snake.turn_down, "Down")
while game_on:
    screen.update()
    snake.follow_consistently()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.reappear()
        snake.new_snake_body()
        score.updated_scoreboard()

    for square in snake.all_squares[1:]:
            if snake.head.distance(square) < 5:
                game_on = False
                GameOver()





screen.exitonclick()
