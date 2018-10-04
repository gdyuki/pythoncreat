import random

Start = True
while Start:
    while True:
        com = random.randint(1,3)
        com_ai = {1:"ぐー", 2:"チョキ", 3:"パー"}
        player = input("じゃんけんしましょう。　ぐーは１　チョキは２　パーは３を入れてね")
        if player == "1" or player == "2" or player == "3":
            player = int(player)
            break
        elif player == "q" :
            Start = False
            break
        else :
            print("有効な数字を入れてください")

    if Start == False :
        break

    if player - com == -1 or player - com == 2 :
        print("相手："+com_ai[com]+"  あなた："+com_ai[player]+"  あなたのかち！！")
    elif player - com == 0:
        print("相手："+com_ai[com]+"  あなた："+com_ai[player]+"  アイコですたね")
    else :
        print("相手："+com_ai[com]+"  あなた："+com_ai[player]+"  あなたの負け")

print("やったぜ")