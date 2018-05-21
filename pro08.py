'''
숨겨진 숫자를 맞추는 게임입니다.
프로그램이 실행되면 1~100 사이의 숫자가 결정됩니다.
사용자가 입력한 숫자가 결정된 숫자보다 높으면 “더 낮게” 출력
사용자가 입력한 숫자가 결정된 숫자보다 낮으면 “더 높게” 출력되며
정답을 맞춘경우 “맞았습니다.” 출력됩니다.
게임을 반복하기 위해 y/n이라 묻고 n인 경우 종료됩니다.
(y 인경우 다시 게임이 시작됩니다.)
'''

import random

num = 0
userNo = 0
choice = 0

while True :

    # for num in range(0, 101):
    num = random.randrange(1, 101)
    print("랜덤생성값: ", num)

    print("=" * 30)
    print("      [숫자맞추기 게임 시작]       ")
    print("=" * 30)

    while True :

        userNo = int(input("숫자: "))

        if userNo>num :
            print("더 낮게")
        elif userNo<num :
            print("더 높게")
        else :
            print("정답입니다.")
            break

    print("게임을 종료하시겠습니까?(y/n)", end=" ")
    choice = input()

    if choice == "y":
        print("=" * 30)
        print("      [숫자맞추기 게임 종료]       ")
        print("=" * 30)
        break
    elif choice == "n":
        continue
