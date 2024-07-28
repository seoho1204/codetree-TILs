a,b=input().split(' ')
a=float(a)
b=float(b)
if a>=1.0 and b>=1.0:
    res='High'
if a>=0.5 and b>=0.5:
    res='Middle'
else:
    res='Low'
print(res)