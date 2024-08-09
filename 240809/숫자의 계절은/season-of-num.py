# 어떤수의 계절이 봄인지 판단하는 함수
# 리턴은 bool 타입이다 true라면 봄이고 false 라면 봄이 아니다. 
def isSpring(num1):
    res = num1>=3 and num1<=5
    return res
# 어떤수의 계절이 여름인지 판단하는 함수
# 리턴은 bool 타입이다 true라면 여름이고 false라면 여름이 아니다
def isSummer(s):
    res = s>=6 and s<=8
    return res
# 어떤수의 계절이 가을인지 판단하는 함수
# 리턴은 bool 타입이다 true라면 가을이고 false라면 가을이 아니다
def isFall(s):
    res = s>=9 and s<=11
    return res




m=int(input())
if isSpring(m):
    res="Spring"
elif isSummer(m):
    res='Summer'
elif isFall(m):
    res='Fall'
else:
    res='Winter'
print(res)