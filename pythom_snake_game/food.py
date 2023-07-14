from turtle import Turtle, write
import random


class Food(Turtle):

     def __init__(self):
         super().__init__()
         self.shape("circle")
         self.penup()
         self.shapesize(stretch_wid=.6, stretch_len=.6)
         self.color("blue")
         self.speed(0)
         self.refresh()
     def refresh(self):
         x = random.randint(-290, 290)
         y = random.randint(-290, 290)
         self.goto(x, y)




