# M>=90
#   L>=95 100000원
#   L>=90 50000원
#   L<90 0원
# M<90 0원
M,L=input().split(' ')
M=int(M)
L=int(L)
if M>=90:
    if L>=95:
        print(100000)
    elif L>=90:
        print(50000)
    else:
        print(0)
    
else:
    print(0)