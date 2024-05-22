grade=int(input())
if grade>=90:
    res='A'
elif grade>=80:
    res='B'
elif grade>=70:
    res='C'
elif grade>=60:
    res='D'
else:
    res='F'
print(res)