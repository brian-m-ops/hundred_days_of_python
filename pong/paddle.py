from turtle import Turtle

STARTING_POSITION = [(350, 0), (-350, 0)]
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1


class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.goto(self.cords)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
