from turtle import*
a=1
b=1
fibonacci=[1,1]
for i in range(6):
  a = a+b
  b = b+a
  fibonacci.append(a)
  fibonacci.append(b)
def fibo_circle(iro,muki,okisa,kakudo,hane,hen):#fibo_circleという名前の関数を作る。
  for i in range(hane):#羽の数だけ繰り返す
    for j in fibonacci:#fibonacciに入っている数で繰り返す
      pencolor(iro)#ペンの色
      pensize(2)#ペンの太さ
      circle(j/okisa,kakudo*muki,hen)
    speed(0)
    penup()#ペンを上にあげる
    home()#ペンの位置をホームに戻す
    pendown()#ペンを下に下げる
    rt(360/hane*(i+1))
fibo_circle('skyblue',1,4,270,8,12)