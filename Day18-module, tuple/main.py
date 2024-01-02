# 세번이상 사용할때
# from turtle import Turtle, Screen
# from turtle import * 는 좋지 않은 방법
# import turtle 한번만 사용할때
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# # 정사각형
# # range 연산자로 4번 반복
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)ㄴ
#     tim.forward(10)
#     tim.pendown()

# # # 다양한 도형그리기
# screen = Screen()
# screen.exitonclick()

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# 다양한 도형 그리기
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# 무작위 행보 구현하기
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed("fastest")

def draw_spirograph(size_of_gaps):
    for _ in range(int(360/size_of_gaps)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()