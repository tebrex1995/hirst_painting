from turtle import Turtle, Screen
import random

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60),
              (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

# 10x10
# dots 20 in size spaces 50 paces
screen = Screen()
t = Turtle()
t.speed("fastest")
t.screen.colormode(255)
t.hideturtle()
t.penup()


def draw_dot():
    t.dot(20, random.choice(color_list))
    t.forward(50)
    t.dot(20, random.choice(color_list))


for _ in range(10):
    for _ in range(9):
        draw_dot()
    t.left(90)
    t.forward(50)
    t.setx(0)
    t.right(90)




screen.exitonclick()
