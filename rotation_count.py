def countRotations(a, low, high):
    if high < low:
        return 0
    if high == low:
        return low
    mid = int(low + (high-low)/2)
    if mid < high and a[mid+1] < a[mid]:
        return mid+1
    if mid > low and a[mid] < a[mid-1]:
        return mid
    if a[high] > a[mid]:
        return countRotations(a, low, mid-1)
    return countRotations(a, mid+1, high)

a = list(map(int, input("Enter the elements of the array: ").split()))
n = len(a)
print("The rotation count of the given rotated sorted array is:", countRotations(a, 0, n-1))
