from turtle import Turtle

# Constants for initial configuration and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # Flag to prevent fast double-key presses causing self-collision
        self.direction_locked = False

    # Create the initial 3-segment body of the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Move the snake forward by shifting segments from tail to head
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Unlock direction changes once per frame loop
    def reset_direction_lock(self):
        self.direction_locked = False

    def up(self):
        if not self.direction_locked and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.direction_locked = True

    def down(self):
        if not self.direction_locked and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.direction_locked = True

    def left(self):
        if not self.direction_locked and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.direction_locked = True

    def right(self):
        if not self.direction_locked and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.direction_locked = True

    # Add a new segment to the snake body
    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    # Extend the snake when eating food
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Reset the snake position and body after a game over
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]