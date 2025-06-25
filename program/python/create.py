import turtle

def dragon_curve(t, order, length, sign=1):
    if order == 0:
        t.forward(length)
    else:
        t.right(45 * sign)
        dragon_curve(t, order - 1, length / (2 ** 0.5), 1)
        t.left(90 * sign)
        dragon_curve(t, order - 1, length / (2 ** 0.5), -1)
        t.right(45 * sign)

# 画面セットアップ
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# 開始位置と方向調整
t.penup()
t.goto(-100, 0)
t.pendown()
t.setheading(0)  # 右向き

# フラクタルを描画（階層の深さと長さ）
dragon_curve(t, order=10, length=200)

# 終了処理
turtle.done()
