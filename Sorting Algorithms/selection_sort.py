def selectionSort(a, n):
    for i in range(n-1):
        small = a[i]
        pos = i
        for j in range(i+1, n):
            if a[j] < small:
                small = a[j]
                pos = j
        a[i], a[pos] = a[pos], a[i]


a = list(map(int, input("Enter the array: ").split()))
selectionSort(a, len(a))

print("The sorted array: ")
for i in a:
    print(i, end=" ")
