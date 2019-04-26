from math import sqrt


def isTriplet(a, n):
    # Squaring all the elements in the array
    for i in range(n):
        a[i] = a[i] * a[i]
    # Sorting the array
    a.sort()

    # Now, We'll fix one element in each iteration and find the other two elements
    for i in range(n-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            if a[j] + a[k] == a[i]:
                print("The pythagorean triplet present in array is", (int(sqrt(a[j])), int(sqrt(a[k])), int(sqrt(a[i]))))
                return True
            else:
                if a[j] + a[k] < a[i]:
                    j = j + 1
                else:
                    k = k - 1
    return False


a = list(map(int, input("Enter an array: ").split()))
if not isTriplet(a, len(a)):
    print("No")
