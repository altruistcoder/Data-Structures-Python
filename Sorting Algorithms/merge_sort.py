def merge(a, l, m, r):
    L = a[l:m+1]
    R = a[m+1:r+1]
    i = 0
    j = 0
    k = l

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1


def mergesort(a, l, r):
    if l < r:
        m = int(l+(r-l)/2)
        mergesort(a, l, m)
        mergesort(a, m+1, r)
        merge(a, l, m, r)


a = list(map(int, input("Enter the array: ").split()))
mergesort(a, 0, len(a)-1)

print("The sorted array: ")
for i in a:
    print(i, end=" ")
