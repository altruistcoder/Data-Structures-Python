def getMaxConsecutiveOne(a, n):
    c = 0 
    res = 0 

    for i in range(0, n):
        if (a[i] == 0):
            c = 0
        else:
            c+= 1 
            res = max(res, c) 
    return res 

a = list(map(int, input("Enter a list of elements: ").split()))
n = len(a)
maxOnes = getMaxConsecutiveOne(a, n)
print("The maximum number of consecutive ones in the array is:", maxOnes)
