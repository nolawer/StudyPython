import random

print("시작")

win = 0
lose = 0
count = 0

def vs():
    global user, npc
    print("user : ", user)
    print("npc : ", npc)

while True:
    try:
        user = int(input("1:가위, 2:바위, 3:보 >>"))
        npc = random.randint(1, 3)
        if 0 < user < 4:
            if user == npc:
                vs()
                print("비겼습니다. 다시 입력하세요.")
                continue
            elif user == 1 and npc == 2:
                vs()
                print("졌다ㅠㅠ")
                count += 1
                lose += 1

            elif user == 1 and npc == 3:
                vs()
                print("이겼다!")
                count += 1
                win += 1

            elif user == 2 and npc == 1:
                vs()
                print("이겼다!")
                count += 1
                win += 1

            elif user == 2 and npc == 3:
                vs()
                print("졌다ㅠㅠ")
                count += 1
                lose += 1

            elif user == 3 and npc == 1:
                vs()
                print("졌다ㅠㅠ")
                count += 1
                lose += 1

            elif user == 3 and npc == 2:
                vs()
                print("이겼다!")
                count += 1
                win += 1
        else:
            print("1,2,3 중 선택해주세요.")

    except(ValueError, ZeroDivisionError):
        print("올바른 선택이 아닙니다. 다시 선택해주세요.")

    print("카운트 : ", count, "전")

    if count == 3:
        winper = round(win / count * 100, 1)
        print("전적 : {} 전 {} 승 {} 패".format(count,win,lose))
        print("승률 : ", winper, "%")
        break
    else:
        continue