#숫자를 입력받아 입력된 숫자만큼 증가하도록 출력하세요.


#숫자 입력받기 - input은 String타입으로 반환되므로 int 형변환 필수!
num = int(input("숫자를 입력하세요: "))

for i in range(1, num+1) :
    #print(i)
    for j in range(1, i+1) :
        print(i, end=" ")
    print()


