n=int(input())
if n<500:
    res="no"
elif n>=500 and n<1000:
    res='pen'
elif n>=1000 and n<3000:
    res='mask'
else:
    res='book'
print(res)