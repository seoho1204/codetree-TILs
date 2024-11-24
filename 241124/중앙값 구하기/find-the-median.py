a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a<b and b<c or c<b and b<a:
    res=b
elif b<a and a<c or c<a and a<b:
    res=a
elif a<c and c<b or b<c and c<a:
    res=c
print(res)