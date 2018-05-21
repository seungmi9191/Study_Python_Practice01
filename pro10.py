'''
“1.예금” 선택후 금액을 입력하면 예금액이 합산됩니다.
“2.출급” 선택후 금액을 입력하면 예금액이 차감됩니다.
“3.잔고” 선택시 현재 잔고가 출력됩니다.
“4.종료” 선택시 종료됩니다.
“1,2,3,4 이외의 숫자” 다시입력해주세요 메시지 출력됩니다.
'''


num = 0 #사용자 번호선택
cash = 0 #입력받는 금액
sumcash = 0 #총 저장된 금액
balance = 0 #잔고

while True :

    print("-"*30)
    print("1.예금 | 2.출금 | 3.잔고 | 4.종료")
    print("-"*30)

    #사용자에게 번호를 입력받음
    num = int(input("선택> "))

    #예금액
    if num==1 :
        cash = int(input("예금액> "))
        sumcash += cash #sum = sum+add

    elif num==2 :
        cash = int(input("출금액> "))
        sumcash -= cash

    elif num==3 :
        balance = sumcash
        print("잔고액>", balance)

    elif num==4 :
        print("프로그램 종료")
        break

    else :
        print("다시 입력해주세요.")


