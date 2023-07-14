from turtle import Turtle, Screen

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.move()
        self.move_up()
        self.move_down()
        self.move_forward()
        self.move_backword()


    def create_snake(self):
        for i in POSITION:
            self.add_one(i)

    def add_one(self, i):
        my_turtle = Turtle("square")
        my_turtle.color("green")
        my_turtle.penup()
        my_turtle.goto(i)
        self.turtles.append(my_turtle)
    def extend(self):
        self.add_one(self.turtles[-1].position())

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)
    def move_down(self):
        if self.turtles[0].heading() != UP:
         self.turtles[0].setheading(DOWN)

    def move_forward(self):
        if self.turtles[0].heading() != LEFT:
          self.turtles[0].setheading(RIGHT)

    def move_backword(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)


