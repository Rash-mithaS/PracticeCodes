#!/bin/python3
# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    valley=0
    for i in range(n):
        if s[i]=='U':
            level+=1
        else:
            level-=1
        if level==0 and s[i]=='U':
            valley+=1
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
