# aM<bM B
# bM<aM A
# aM==bM
#   aE<bE B
#   bE<aE A
aM,aE=map(int,input().split(' '))
bM,bE=map(int,input().split(' '))
if aM<bM:
    print('B')
elif bM<aM:
    print('A')
else:
    if aE<bE:
        print('B')
    elif bE<aE:
        print('A')