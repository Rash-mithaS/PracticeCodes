#!/bin/python3

# Complete the superDigit function below.
def superDigit(n):
    if int(n) > 9:
            su=0
            for i in range(len(n)):
                su += int(n[i])
                #print(su)
            n=str(su)
            #print('n',n)
            superDigit(n)
    else:
            #print('l')
        print(int(n))
    
nk = input().split()

n = nk[0]

k = int(nk[1])
n=str(n)
su=0
for i in range(len(n)):
    su+=int(n[i])
n=str(su*k)
result = superDigit(n)



    
    
