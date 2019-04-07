def bubbleSort(a, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


a = list(map(int, input("Enter the array: ").split()))
bubbleSort(a, len(a))

print("The sorted array: ")
for i in a:
    print(i, end=" ")
