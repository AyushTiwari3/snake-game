from turtle import Turtle,Screen
import time
from day20snakeclass import Snake
from day21_food import Food
from day21_scoreboard import ScoreBoard
starting_postions=[(0,0),(-20,0),(-40,0)]
segments=[]
my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("Snakeuuiiiiuuu")
my_screen.tracer(0)
scoreboard=ScoreBoard()
snake=Snake()
food=Food()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
        my_screen.update()
        time.sleep(.1)
        snake.move()

        if snake.head.distance(food)<15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()
                # size=snake.size_inc()

        if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
                game_is_on=False
                scoreboard.game_over()

        for segment in snake.segments[1:]:
                if snake.head.distance(segment)<10:
                        game_is_on=False
                        scoreboard.game_over()
my_screen.exitonclick()
