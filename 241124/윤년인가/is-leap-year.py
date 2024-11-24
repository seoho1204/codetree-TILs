# y를 입력받는다
# 4로 나누어 떨어지면 true
# else false
# 100으로 나누어 떨어지면서 400으로 나누어 떨어지지 않으면 false

y=int(input())
if y%4==0:
    if y%100==0 and y%400!=0:
        res='false'
    res='true'
else:
    res='false'

print(res)