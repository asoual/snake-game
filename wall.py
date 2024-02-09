from turtle import Turtle 

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-290,-290)
        self.pendown()
        self.goto(290,-290)
        self.goto(290,290)
        self.goto(-290,290)
        self.goto(-290,-290)