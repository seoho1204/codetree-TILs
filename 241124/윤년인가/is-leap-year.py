# y를 입력받는다
# 4로 나누어 떨어지면 true
# else false
# 100으로 나누어 떨어지면서 400으로 나누어 떨어지지 않으면 false

y=int(input())
if y%4==0:
    if y%100==0 and y%400!=0:
        res='false'
    else:
        res='true'
else:
    res='false'

print(res)


# y가 4의배수면
#   y가 100의배수 면서 400의 배수가 아님
#       평년
#   아니면
#       윤년
#아니면
#   평년