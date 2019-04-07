def insertionSort(a, n):
    for i in range(1, n):
        t = a[i]
        j = i-1
        while t < a[j] and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = t


a = list(map(int, input("Enter the array: ").split()))
insertionSort(a, len(a))
print("The sorted array: ")
for i in a:
    print(i, end=" ")
