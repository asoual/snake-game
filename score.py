from turtle import Turtle 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highest_score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
    
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,320)
        self.update_score()
            
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highest_score}", align="center", font=("Verdana", 15, "normal"))
            
    def increase_score(self):
        self.score += 1
        self.update_score()
    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode ="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()
    def game_over(self):
        self.clear()
        self.update_score()
        self.goto(0,0)
        self.write(f" Game Over: Your final score is {self.score}",align= "center",font=("Verdana", 15, "normal"))
