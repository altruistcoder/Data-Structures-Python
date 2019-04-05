def oneswapSort(a, n):
    first = 0
    second = 0
    c = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            c += 1
            if first == 0:
                first = i
            else:
                second = i
    if c > 2:
        return False

    if c == 0:
        return True

    if c == 2:
        a[first-1], a[second] = a[second], a[first-1]

    elif c == 1:
        a[first - 1], a[first] = a[first], a[first - 1]

    for i in range(1, n):
        if a[i] < a[i-1]:
            return False
    return True


a = list(map(int, input("Enter an array: ").split()))
if oneswapSort(a, len(a)):
    print("Yes")
else:
    print("No")
