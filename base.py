import random

invest = input()
invest = int(invest)
mycoin = invest//21.7391304
print(mycoin)

bet_3 = [0]*508
bet_3.append(1)
bet_3.append(1)
bet_3.append(2)
bet_3.append(2)

greap =[0]*73
for i in range(16):
    greap.append(1)
for i in range(3):
    greap.append(2)

for i in range(5000):
    lottery = random.choice(bet_3)
    if lottery == 1: 
        gain =  248
        result = "BIG"
    elif lottery == 2:
        gain = 93
        result = "REG"
    elif lottery ==0:
        small_lottery = random.choice(greap)
        if small_lottery == 1:
            gain =  5
            result = "ブドウ"
        elif small_lottery == 2:
            gain = -1
            result = "チェリー"
        else:
            gain =  - 3
            result = "なし"
    mycoin = mycoin + gain
    yen = mycoin*20 - invest
    if yen > 0:
        winlose = "勝ち*******************"
    else:
        winlose = "負け"
    if mycoin < 0:
        break
    print("持ちメダル"+ str(mycoin) + " 今 " +str(i + 1) +"回転目  "+ "役："+result , str(abs(yen)) +"円"+ winlose)


