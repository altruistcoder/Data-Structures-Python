def minSwapping(a, n):
    res = 0
    temp = a.copy()
    ihash = {}
    temp.sort()
    for i in range(n):
        ihash[a[i]] = i
    start = 0
    for i in range(n):
        if (a[i] != temp[i]):
            res += 1
            start = a[i]
            a[i], a[ihash[temp[i]]] = a[ihash[temp[i]]], a[i]
            ihash[start] = ihash[temp[i]]
            ihash[temp[i]] = i
    return res

a = list(map(int, input("Enter the elements of the input array: ").split()))
res = minSwapping(a, len(a))
print("The  minimum number of steps required for sorting:", res)