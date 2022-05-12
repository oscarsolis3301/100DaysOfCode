from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.current_y = 1
        self.current_x = 1
        self.current_speed = 1

    def flipy(self):
        self.current_y *= -1

    def flipx(self):
        self.current_x *= -1

    def move(self):
        self.goto((self.xcor() + self.current_x), (self.ycor() + self.current_y))

    def reset(self):
        self.goto(0, 0)
        self.flipx()

# def move(self):
#     self.goto((self.ycor() + self.movement), (self.xcor() + self.movement))
#
# def bounce_y(self):
#     if self.ycor() > 200:
#         self.goto((self.ycor() - self.movement), (self.xcor() + self.movement))
#     else:
#         self.goto((self.ycor() + self.movement), (self.xcor() + self.movement))

# def bounce_x(self):
#     self.goto((self.ycor() - self.movement), (self.xcor() - self.movement))
#
# def move_up(self, plane):
#     if plane == "x":
#         pass
#     else:
#         self.sety(self.ycor() + 1)
#         self.setx(self.xcor() + 1)
#
# def move_down(self, plane):
#     if plane == "x":
#         pass
#     else:
#         self.sety(self.ycor() - 1)
#         self.setx(self.xcor() + 1)
#
# def move_down_x(self, plane):
#     if plane == "x":
#         pass
#     else:
#         self.sety(self.ycor() - 1)
#         self.setx(self.xcor() - 1)
#
# def bounce(self, plane):
#
#     if plane == "x":
#         self.sety(self.ycor() - self.movement)
#     else:
#         if not self.touched_top:
#             if self.ycor() != 280 and -340 < self.xcor() <= 340:
#                 print("First if satement")
#                 self.move_up("y")
#             elif self.ycor() == 280 and -340 < self.xcor() <= 340:
#                 print("Second if")
#                 self.touched_top = True
#         else:
#             if self.ycor() != -280 and -360 < self.xcor() <= 360:
#                 self.move_down("y")
#             elif self.ycor() == -280 and -360 < self.xcor() <= 360:
#                 self.touched_top = False
#
