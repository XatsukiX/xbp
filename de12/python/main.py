for i   in range(1,4):
    print(i,"人目")
    #input関数
    #intは整数、floatは少数もおｋ
    name=input("名前を入れてください！")
    waist=float(input("腹囲を入力してください"))
    age=int(input("年齢を入力してください"))

    #方程式っぽい
    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    #条件分岐 #命題っぽい
    if waist>=85 and age>=40:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")