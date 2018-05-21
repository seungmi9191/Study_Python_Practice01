'''
5개의 숫자를 키보드로 입력받아 평균을 구하는 프로그램을 작성하세요
숫자는 콤마(,) 로 구분하여 입력합니다.
'''

#키보드로 숫자 입력받기
num = input("숫자 5개를 ,로 구분하여 입력하세요: ")
print(num, type(num))

#split로 문자열을 자르면 return으로 list를 반환해준다.
#함수에는 return값이 각각 다르게 있다.
number = num.split(",")
print(number)

sum = 0

#리스트에 넣어줬기 때문에 리스트 사용 가능
#str이기 때문에 int로 형변환 해줘야 함
for i in number:
    sum += int(i)

#나중에 가변적으로 변할 것을 대비하여 len 메소드를 통해 number의 길이를 나타낼 수 있다.
print(sum/len(number))