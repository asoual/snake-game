from turtle import Turtle

SQUARE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in SQUARE_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(0.8,0.8)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move (self):
        for segment in range (len(self.segments)-1, 0, -1):
            new_x = self.segments[segment -1].xcor()
            new_y = self.segments[segment -1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)   
        
    def move_left(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180)
            
    def move_right(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0)
            
    def move_up(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)
            
    def move_down(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(270)
