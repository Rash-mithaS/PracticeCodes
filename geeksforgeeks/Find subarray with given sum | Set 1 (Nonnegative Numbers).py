"""
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
Examples :

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4
Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There is no subarray with 0 sum

"""
def subArraySum(arr, n, sum):
    # Pick a starting
    subsum=0
    p1=p2=0 #set pointers 1 and 2


    if sum!=0:
        while p1 < n:

            if subsum == sum:
                print("Sum found between indexes %d and %d" % (p2, p1 - 1))
                return 1 #exit program
            elif subsum > sum:
                subsum -= arr[p2] #subtract the element p2 is pointing to
                p2 += 1           #increment p2
            else:
                subsum += arr[p1] #add the element p2 is pointing to
                p1 += 1           #increment p1

    print("No subarray found")
    return 0


# Driver program
arr = [1, 4, 20, 3, 10, 5]
n = len(arr)
sum = 33

subArraySum(arr, n, sum)
