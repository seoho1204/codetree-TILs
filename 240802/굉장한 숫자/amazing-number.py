n=int(input())
if (n%2==1 and n%3==0) or (n%2==0 and n%5==0):
    res='true'
else:
    res='false'
print(res)