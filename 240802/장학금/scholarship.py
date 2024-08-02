#a,b input a=90 이상  95 이상 10만원 90점 이상 5만원 else x 
a,b=input().split(' ')
a=int(a)
b=int(b)
if a>=90:
    if b>=95:
        res=100000
    elif b>=90:
        res=50000
else:
    res=0
print(res)