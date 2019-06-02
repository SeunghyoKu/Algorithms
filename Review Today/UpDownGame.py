#숫자 맞추기 게임! Up & Down game!!
import random

#1~100까지의 숫자중 하나 랜덤 생성하기
randnum = random.randrange(1,100)


while True:
    #값을 입력 받는다.
    a = int(input("1부터 100까지의 숫자를 입력하세요!"))
    
    #랜덤 생성 숫자가 입력한 값과 다를 경우
    if a != randnum:
        if a < randnum:
            if randnum - a < 5:
                 print("조금 작아요!")
            else:
                print("너무 작아요!")

        elif a > randnum:
            if a - randnum < 5:
                print("조금 커요!")
            else:
                print("너무 커요!")

    #답을 맞췄을 경우
    else:
        print("정답!")
        break
