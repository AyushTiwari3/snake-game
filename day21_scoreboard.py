from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        # self.clear()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ",align="center",font=("Courier",20,"normal"))

    def increase_score(self):
       self.score+=1
       self.clear()
       self.update_scoreboard() 
        
    def game_over(self):
        
        self.goto(0,0)
        self.write(f"GAME OVER ",align="center",font=("Courier",25,"normal")) 