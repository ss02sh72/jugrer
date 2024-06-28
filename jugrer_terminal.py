import random
from imgcat import imgcat
import numpy as np

print("投資金額を入力してください")
invest = input() 
invest = int(invest)
print("エンターを押して回転")
mycoin = invest//21.7391304
setting_list = list(range(1, 7))
setting = random.choice(setting_list)

n = 1

def Lottery(setting):
    if setting == 6:

        bet_6 = random.randint(1, 261120)

        if 1 <= bet_6 < 35771:
            gain = 0
            role = "リプレイ"
        elif 35771 <= bet_6 < 36027:
            gain = 7
            role = "ピエロ"
        elif 36027 <= bet_6 < 36282:
            gain = 11
            role = "ベル"
        elif 36282 <= bet_6 < 44140:
            gain = -1
            role = "チェリー"
        elif 44140 <= bet_6 < 87158:
            gain = 5
            role = "ブドウ"
        elif 87158 <= bet_6 < 88182:
            gain = -1
            role = "REG"
            print("ボーナス開始")
        elif 88182 <= bet_6 < 89206:
            gain = -1
            role = "BIG"
            print("ボーナス開始")
        else:
            gain = -3
            role = "役なし"

    if setting == 5:

        bet_5 = random.randint(1, 261120)

        if 1 <= bet_5 < 35771:
            gain = 0
            role = "リプレイ"
        elif 35771 <= bet_5 < 36027:
            gain = 7
            role = "ピエロ"
        elif 36027 <= bet_5 < 36282:
            gain = 11
            role = "ベル"
        elif 36282 <= bet_5 < 44140:
            gain = -1
            role = "チェリー"
        elif 44140 <= bet_5 < 87516:
            gain = 5
            role = "ブドウ"
        elif 87516 <= bet_5 < 88540:
            gain = -1
            role = "REG"
            print("ボーナス開始")
        elif 88540 <= bet_5 < 89547:
            gain = -1
            role = "BIG"
            print("ボーナス開始")
        else:
            gain = -3
            role = "役なし"


    if setting == 4:

        bet_4 = random.randint(1, 261120)

        if 1 <= bet_4 < 35771:
            gain = 0
            role = "リプレイ"
        elif 35771 <= bet_4 < 36027:
            gain = 7
            role = "ピエロ"
        elif 36027 <= bet_4 < 36282:
            gain = 11
            role = "ベル"
        elif 36282 <= bet_4 < 44140:
            gain = -1
            role = "チェリー"
        elif 44140 <= bet_4 < 87516:
            gain = 5
            role = "ブドウ"
        elif 87516 <= bet_4 < 88346:
            gain = -1
            role = "REG"
            print("ボーナス開始")
        elif 88346 <= bet_4 < 89354:
            gain = -1
            role = "BIG"
            print("ボーナス開始")
        else:
            gain = -3
            role = "役なし"

    if setting == 3:

        bet_3 = random.randint(1, 261120)

        if 1 <= bet_3 < 35771:
            gain = 0
            role = "リプレイ"
        elif 35771 <= bet_3 < 36027:
            gain = 7
            role = "ピエロ"
        elif 36027 <= bet_3 < 36282:
            gain = 11
            role = "ベル"
        elif 36282 <= bet_3 < 44140:
            gain = -1
            role = "チェリー"
        elif 44140 <= bet_3 < 87516:
            gain = 5
            role = "ブドウ"
        elif 87516 <= bet_3 < 88305:
            gain = -1
            role = "REG"
            print("ボーナス開始")
        elif 88305 <= bet_3 < 89272:
            gain = -1
            role = "BIG"
            print("ボーナス開始")
        else:
            gain = -3
            role = "役なし"
 

    if setting == 2:

        bet_2 = random.randint(1, 261120)

        if 1 <= bet_2 < 35771:
            gain = 0
            role = "リプレイ"
        elif 35771 <= bet_2 < 36027:
            gain = 7
            role = "ピエロ"
        elif 36027 <= bet_2 < 36282:
            gain = 11
            role = "ベル"
        elif 36282 <= bet_2 < 44140:
            gain = -1
            role = "チェリー"
        elif 44140 <= bet_2 < 87516:
            gain = 5
            role = "ブドウ"
        elif 87516 <= bet_2 < 88170:
            gain = -1
            role = "REG"
            print("ボーナス開始")
        elif 88170 <= bet_2 < 89137:
            gain = -1
            role = "BIG"
            print("ボーナス開始")
        else:
            gain = -3
            role = "役なし"


    if setting == 1:

        bet_1 = random.randint(1, 261120)

        if 1 <= bet_1 < 35771:
            gain = 0
            role = "リプレイ"
        elif 35771 <= bet_1 < 36027:
            gain = 7
            role = "ピエロ"
        elif 36027 <= bet_1 < 36282:
            gain = 11
            role = "ベル"
        elif 36282 <= bet_1 < 44140:
            gain = -1
            role = "チェリー"
        elif 44140 <= bet_1 < 87516:
            gain = 5
            role = "ブドウ"
        elif 87516 <= bet_1 < 88111:
            gain = -1
            role = "REG"
            print("ボーナス開始")


        elif 88111 <= bet_1 < 89067:
            gain = -1
            role = "BIG"
            print("ボーナス開始")
        else:
            gain = -3
            role = "役なし"

        
    result = [gain, role]





    return result

def Bonus():
    bonus_list = ["ブドウ", "チェリー"]
    user_input_2 = input()
    if not user_input_2.strip():
        result = [12, random.choice(bonus_list), "ボーナス中**********"]
    return result
        


for i in range(5000):
    user_input = input()
    if not user_input.strip():

        jug_list = Lottery(setting)
        jug_list.append(n)
        n = n + 1
        mycoin = mycoin + jug_list[0]
        if mycoin < 0:
            print("持ちメダルがなくなりました")
            print("設定は" + str(setting) + "でした。")
            break

        print(str(jug_list[0] + 3) + "　　" + jug_list[1] +"　　" + str(jug_list[2]) + "回転")
        print("持ちメダル：" + str(mycoin))

        if jug_list[1] == "REG":
            for i in range(8):
                bonus = Bonus()
                print(str(bonus[0] +2 ) +"　　"+ bonus[1] +"　　"+ bonus[2])
                mycoin = mycoin + 12
                print("持ちメダル：" + str(mycoin))
            print("ボーナス終了")

        if jug_list[1] == "BIG":
            for i in range(21):
                bonus = Bonus()
                print(str(bonus[0] +2 ) +"　　"+ bonus[1] +"　　"+ bonus[2])
                mycoin = mycoin + 12
                print("持ちメダル：" + str(mycoin))
            print("ボーナス終了")
                
            n = 1
        
    else:
        print(str(mycoin*20) + "円の換金")
        print("設定は" + str(setting) + "でした。")
        break

        




        

        

