#키보드로 정수 수치를 입력받아 짝수인지 홀수인지 판별하는 코드를 작성하세요.
#입력받은 수치가 숫자인지도 판별하여 숫자가 아닌경우 "숫자가 아닙니다."라고 출력합니다.


#함수로 빼서 사용해보기~

num=""

#짝수 입력시
try :
    num = int(input("수를 입력하세요: "))
    if num % 2 == 0:
        print("짝수")
    elif num % 2 == 1:
        print("홀수")
except ValueError : #에러종류
    print("숫자가 아닙니다.".format(num))


