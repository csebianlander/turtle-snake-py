from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_XPOS = 0
MOVE_DISTANCE = 20
LENGTH = 3

class Snake:
    def __init__(self):
        self.xpos = STARTING_XPOS
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for _ in range(LENGTH):
            self.add_segment((self.xpos, 0))
            self.xpos -= MOVE_DISTANCE

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)