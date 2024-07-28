a=float(input())
b=float(input())
if a>=1.0 and b>=1.0:
    res='High'
elif a>=0.5 and b>=0.5:
    res='Middle'
else:
    res='Low'
print(res)