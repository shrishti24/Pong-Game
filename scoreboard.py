from turtle import Turtle

FONT = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def draw_line(self):
        self.pen(pencolor="white", pensize=5)
        self.penup()
        self.goto(0, 280)
        self.setheading(270)
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def update_score(self):
        self.clear()

        self.goto(100, 180)
        self.write(self.l_score, move=False, align="center", font=FONT)
        self.goto(-100, 180)
        self.write(self.r_score, move=False, align="center", font=FONT)
        self.draw_line()

    def l_scores(self):
        self.l_score += 1
        self.update_score()


    def r_scores(self):
        self.r_score += 1
        self.update_score()
