tmp=int(input())
if tmp<0:
    res='ice'
elif tmp>=100:
    res='vapor'
else:
    res='water'
print(res)