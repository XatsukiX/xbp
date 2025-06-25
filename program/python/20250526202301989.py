import turtle

#初期設定
screen=turtle.Screen()
screen.bgcolor("white")
pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()

#関数定義
def draw_triangle_outline(length,depth):
    if depth == 0:
        return
    for _ in range(3):
        pen.forward(length)
        pen.left(120)
        draw_triangle_outline(length/2,depth-1)

pen.penup()
pen.goto(-200,-170)
pen.setheading(0)
pen.pendown()
draw_triangle_outline(400,8)