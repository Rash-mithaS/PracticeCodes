#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs=0
    flag=0
    ar.sort()

    for i in range(len(ar)-1):
        if (flag == 0 and ar[i]==ar[i+1]):
            flag = 1
            pairs += 1
        elif flag==1:
            flag=0
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
