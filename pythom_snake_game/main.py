from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

game_screen = Screen()
game_screen.setup(600, 600)
game_screen.bgcolor("black")
game_screen.title("my snake game")
game_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game_screen.listen()
game_screen.onkey(snake.move_up, "w")
game_screen.onkey(snake.move_down, "s")
game_screen.onkey(snake.move_backword, "a")
game_screen.onkey(snake.move_forward, "d")

game_is_on = True

# def score(self, z=0):
#     z += 1
#     game_screen.clear()
#
#     write(f"Score: {z}", align="center", font=("Arial", 24, "normal"))


while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280:
        game_is_on = False
        score.end()

    if snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() > 280:
        game_is_on = False
        score.end()
    for turtle in snake.turtles[1:]:

        if snake.turtles[0].distance(turtle) < 10:
            game_is_on = False
            score.end()

game_screen.exitonclick()
