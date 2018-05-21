'''
파이썬 경로명 s = "/usr/local/bin/python.exe"을 이용하여
아래와 같이 출력해보세요.

user,local,bin,python.exe
/usr/local/bin,pyhon.exe
'''

s = "/usr/local/bin/python.exe"

s = s.split("/") #자르는 연습해보기
s = ",".join(s)
s = s.replace(",","",1)

print(s)

print("-"*30)

s = "/usr/local/bin/python.exe"
s1 = s[:14]
s2 = s[14:]
s2 = s2.replace("/",",")
print(s1+s2)
