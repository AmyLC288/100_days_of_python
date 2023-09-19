from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body_parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_part(position)
    def add_body_part(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_body_parts.append(snake_body)
    def move(self):
        for body_part_no in range(len(self.snake_body_parts) - 1, 0, -1):
            new_x = self.snake_body_parts[body_part_no - 1].xcor()
            new_y = self.snake_body_parts[body_part_no - 1].ycor()
            self.snake_body_parts[body_part_no].goto(new_x, new_y)
        self.snake_body_parts[0].forward(DISTANCE)

    def up(self):
        if self.snake_body_parts[0].heading() != DOWN:
            self.snake_body_parts[0].setheading(UP)
    def down(self):
        if self.snake_body_parts[0].heading() != UP:
            self.snake_body_parts[0].setheading(DOWN)
    def left(self):
        if self.snake_body_parts[0].heading() != RIGHT:
            self.snake_body_parts[0].setheading(LEFT)

    def right(self):
        if self.snake_body_parts[0].heading() != LEFT:
             self.snake_body_parts[0].setheading(RIGHT)



    def extend(self):
        self.add_body_part(self.snake_body_parts[-1].position())