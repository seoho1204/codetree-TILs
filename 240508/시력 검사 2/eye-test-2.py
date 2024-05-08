vision=float(input())
if vision>=1.0:
    res='High'
elif vision>=0.5:
    res='Middle'
else:
    res='Low'
print(res)