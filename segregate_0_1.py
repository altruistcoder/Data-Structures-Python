def segregate_0_1(a, n):
    x = 0
    y = n-1
    while x < y:
        if a[x] == 1:
            a[x], a[y] = a[y], a[x]
            y -= 1
        else:
            x += 1
    return a


a = list(map(int, input("Enter a list of elements: ").split()))
n = len(a)
r = segregate_0_1(a, n)
print("The segregated array is:")
[print(a[i], end=" ") for i in range(n)]
