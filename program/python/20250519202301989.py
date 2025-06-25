import random

def get_pi(darts):#ダーツは引数の中に入れる
    in_circle=0
    for _ in range(darts):#i か_ forの後
        x=random.random()
        y=random.random()
        if x**2 + y**2 < 1:
            in_circle +=1 #　+=は一ずつ足す
    return in_circle / darts * 4

print(get_pi(40000))