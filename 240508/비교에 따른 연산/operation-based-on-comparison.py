a,b=map(int,input().split(' '))
if b<a:
    res=a*b
    print(res)
else:
    res=b//a
    print(res)