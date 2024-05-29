a=int(input())
if a%2==0:
    res=a//2
if res%2==1:
    res=(res+1)//2
print(res)