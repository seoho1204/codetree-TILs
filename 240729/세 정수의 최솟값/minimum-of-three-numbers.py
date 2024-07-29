a,b,c=map(int,input().split(" "))
if a<=b and a<=c:
    res=a
elif b<=a and b<=c:
    res=b
else:
    res=c
print(res)