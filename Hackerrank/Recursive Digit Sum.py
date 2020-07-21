#!/bin/python3

# Complete the superDigit function below.
def superDigit(n):
    if int(n) > 9:
            sumtotal=0
            for i in range(len(n)):
                sumtotal += int(n[i])
                
            n=str(sumtotal)
            
            superDigit(n)
    else:
            
        print(int(n))
    
nk = input().split()

n = nk[0]

k = int(nk[1])
n=str(n)
sumtotal=0
for i in range(len(n)):
    sumtotal+=int(n[i])
n=str(sumtotal*k)
result = superDigit(n)



    
    
