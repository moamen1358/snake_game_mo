from turtle import Turtle


class Score(Turtle):
     def __init__(self):
         super().__init__()
         self.score = 0
         self.penup()
         self.color("white")

         self.hideturtle()
         self.update()

     def update(self):
         self.goto(0, 265)
         self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

     def increase_score(self):
         self.score += 1
         self.clear()
         self.update()
     def end(self):
         self.goto(0, 0)
         self.clear()
         self.write(f"Game Over .  your score is {self.score}", align="center", font=("Arial", 24, "normal"))
