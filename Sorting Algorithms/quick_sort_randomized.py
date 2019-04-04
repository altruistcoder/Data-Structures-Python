from random import randint


def partition(a, l, h):
    pivot = a[h]
    i = l-1
    for j in range(l, h):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[h] = a[h], a[i+1]
    return i+1


def random_partition(a, l, h):
    r = randint(l, h-1)
    a[h], a[r] = a[r], a[h]
    return partition(a, l, h)


def quicksort(a, l, h):
    if l < h:
        p = random_partition(a, l, h)
        quicksort(a, l, p-1)
        quicksort(a, p+1, h)


a = list(map(int, input("Enter the array: ").split()))
quicksort(a, 0, len(a)-1)

print("The sorted array: ")
for i in a:
    print(i, end=" ")
