def removeDuplicates(a, n):
    if n == 0 or n == 1:
        return n
    j = 0
    for i in range(0, n-1):
        if a[i] != a[i+1]:
            a[j] = a[i]
            j += 1
    a[j] = a[n - 1]
    j += 1
    return j


a = list(map(int, input("Enter a list of elements: ").split()))
n = len(a)
m = removeDuplicates(a, n)

print("The resultant array is:")
[print(a[i], end=" ") for i in range(m)]
