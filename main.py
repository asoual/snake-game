from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from wall import Wall
import time

screen = Screen()
screen.listen()
screen.setup(width=750, height=750)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
wall = Wall()

screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)
screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Down",fun=snake.move_down)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food 
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.increase_score()
    # detect collision with wall 
    if abs(snake.head.xcor())>280 or abs(snake.head.ycor())>280:
        # game_is_on = False
        score.reset_score()
        snake.reset_snake()
        # score.game_over()
    # detect collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            # game_is_on = False
            score.reset_score()
            snake.reset_snake()
            # score.game_over()
screen.exitonclick()