#구구단 출력하세요.

i, j = 0, 0

for i in range(1, 10, 1) :
    for j in range(2, 10, 1) :
        print("%d * %d = %d" %(j,i,i*j), end="\t")
    print(" ")
