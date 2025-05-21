from turtle import Turtle
#creating constants for easy data entry
ALIGNMENT = "center"
FONT = ("courier", 16, "normal")

class Scoreboard(Turtle): #'Scoreboard' is a subclass and 'Turtle' is a superclass

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle() #hiding the unnecessary turtle
        self.goto(0, 270)  # near top of screen
        self.update_scoreboard()

    def update_scoreboard(self): #to keep from new score from overlapping the previous one
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self): #to increase the score everytime there's a collision of snake and food
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)