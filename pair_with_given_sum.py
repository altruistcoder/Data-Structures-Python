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


def hasPair(a, n, s):
    # Sorting the array
    mergesort(a, 0, n-1)
    l = 0
    r = n - 1

    # Traversing the array for finding the suitable pair
    while l < r:
        if a[l] + a[r] == s:
            print("The suitable pair is", (a[l], a[r]))
            return 1
        elif a[l] + a[r] < s:
            l += 1
        else:
            r -= 1
    return 0


a = list(map(int, input("Enter the values of the array: ").split()))
s = int(input("Enter the value of sum to be find: "))
if not hasPair(a, len(a), s):
    print("Pair not present in the array whose sum is equal to", s)
