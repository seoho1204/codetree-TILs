m=int(input())
if m>=3 and m<=5:
    res="Spring"
elif m>=6 and m<=8:
    res='Summer'
elif m>=9 and m<=11:
    res='Fall'
else:
    res='Winter'
print(res)