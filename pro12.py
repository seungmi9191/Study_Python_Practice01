#주어진 문자열의 공백을 콤마(,)로 변경 후 출력하세요.

s = "This is a pencil"

#원래 문자열 출력
print(s)

print("-"*30)

#공백기준으로 문자열 자름(변수 새로 둘까하다가 원본을 바꾸고 싶었음)
s = s.split()
print(s)

print("-"*30)

#,를 이용하여 문자열 다시 붙여줌

s = ",".join(s)
print(s)

#replace로 공백을 ","로 대체하는 시도는 먹히지않음 -> 방법을 다시 찾아보기