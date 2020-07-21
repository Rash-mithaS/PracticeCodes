#!/bin/python3

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c=sorted(c)
    
    maxi = c[0]

    for i in range(len(c)):
        if i == len(c) - 1:
            m = abs((c[i] - (n-1)))
            
        else:
            m=abs(c[i]-c[i+1])//2
            
        if m > maxi:
            maxi = m
    return maxi
   

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
