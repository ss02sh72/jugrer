import random
import numpy as np




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
            gain = 93
            role = "REG"
        elif 88182 <= bet_6 < 89206:
            gain = 248
            role = "BIG"
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
            gain = 93
            role = "REG"
        elif 88540 <= bet_5 < 89547:
            gain = 248
            role = "BIG"
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
            gain = 93
            role = "REG"
        elif 88346 <= bet_4 < 89354:
            gain = 248
            role = "BIG"
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
            gain = 93
            role = "REG"
        elif 88305 <= bet_3 < 89272:
            gain = 248
            role = "BIG"
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
            gain = 93
            role = "REG"
        elif 88170 <= bet_2 < 89137:
            gain = 248
            role = "BIG"
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
            gain = 93
            role = "REG"
        elif 88111 <= bet_1 < 89067:
            gain = 248
            role = "BIG"
        else:
            gain = -3
            role = "役なし"

        
    result = [gain, role]

    return result

k = 0
p = 0
sum = 0
print("投資金を入力してください")
first_invest = input()
for i in range(100000):#入店回数
    my_coin = int(first_invest)//21.7391304
    i = i + 1
    result_end = []
    for l in range(1000):
        setting_list = list(range(1, 7))
        setting = random.choice(setting_list)
        jug_result = Lottery(setting)
        my_coin = my_coin + jug_result[0]
        result_end = [l, my_coin, setting]
        if my_coin < 0:
            break
        if jug_result[0] == 93 or  jug_result[0] == 248:
            p = p + 1
            if my_coin*20 > int(first_invest):
                k = k + 1
            sum = sum + my_coin*20
            break
    # print(str(result_end[0]) + " 回転、" + str(result_end[1]*20) + "円換金、" + "設定" + str(result_end[2]))


print("勝率；" + str((100*k)//i)+ "％　" + "(" + str(k) + ")　ぺかった確率:"   + str((100*p)//i) + "％　" + "(" + str(p) + ")　"+ str(i) + "回入店　" + "期待値：" + str(sum//i) + "円")

        









        

        

