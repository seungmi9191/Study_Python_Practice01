'''
주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 아래와 같이 출력하세요
	data = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31 ]
'''

data = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31]
#갯수를 구할 변수
count = 0
#합계를 구할 변수
sum = 0

for multiple in data :
   # print(multiple)

    if multiple%3==0 :
        #print("3의 배수:" , multiple, end="\t")
        #3의 배수이면 count에 1을 더해줌
        count += 1
        #3의 배수이면 sum에 더함
        sum += multiple

print("주어진 리스트에서 3의 배수의 개수=> %d" %count)
print("주어진 리스트에서 3의 배수의 합=> %d" %sum)














