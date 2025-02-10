def getMaxLength(a, n):

    c = 0 
    res = 0 

    for i in range(0, n):
        if (arr[i] == 0):
            c = 0
        else:
            c+= 1 
            res = max(res, c) 
    return res 

a = list(map(int, input("Enter a list of elements: ").split()))
n = len(a)
print(getMaxLength(a, n))
