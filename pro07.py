'''
a. 입력 받은 숫자가 홀수인 경우에는, 입력 값까지 홀수의 합을 출력합니다.
- 예) 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
b. 입력 받은 숫자가 짝수인 경우에는, 입력 값까지 짝수의 합을 출력합니다.
    - 예) 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )
'''
num, startNum, i, sum = 0, 0, 0, 0

print("숫자를 입력하세요.: ", end=" ")
num = int(input())

if num%2==1 :
    startNum = 1
elif num%2==0 :
    startNum = 2

for i in range(startNum, num+1, i+2) :
    sum += i

print("결과값: %d" %sum)