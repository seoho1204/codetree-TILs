gender=int(input())
age=int(input())
if gender==0:
    if age>=19:
        res='MAN'
    elif age<19:
        res='BOY'

elif gender==1:
    if age>=19:
        res='WOMAN'
    elif age<19:
        res='GIRL'

print(res)




# 성별 입력받기
# 나이 입력받기

#만약 남자라면
#    만약19세 이상이라면
#       남자
#   만약 19세 미만이라면
#       소년
# 여자
#   19세 이상
#       여자
#   19세 미만
#       소녀
#
#
#