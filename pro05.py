#정수 5개를 입력받아 가장 큰 수를 출력하세요. (리스트 없이 변수로만 구하세요.)

count = 0
max = 0

print("숫자를 입력하세요. \n")

print("숫자:", end=" ")
no1 = int(input())

print("숫자:", end=" ")
no2 = int(input())

print("숫자:", end=" ")
no3 = int(input())

print("숫자:", end=" ")
no4 = int(input())

print("숫자:", end=" ")
no5 = int(input())

if no1>=no2 and no1>=no3 and no1>=no4 and no1>=no5 :
    max = no1
elif no2>=no1 and no2>=no3 and no2>=no4 and no2>=no5 :
    max = no2
elif no3>=no1 and no3>=no2 and no3>=no4 and no3>=no5 :
    max = no3
elif no4>=no1 and no4>=no2 and no4>=no3 and no4>=no5 :
    max = no4
elif no5>=no1 and no5>=no2 and no5>=no3 and no5>=no4 :
    max = no5

print("최대값은 %d입니다." %max)