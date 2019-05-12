def secondLargest(a, n):
    if n < 2:
        print("No. of elements in array are less than two")
        return
    first = second = -2147483648
    for i in range(n):
        # If current element is smaller than first then update both first and second
        if a[i] > first:
            second = first
            first = a[i]
        # If a[i] is in between first and second then update second
        elif a[i] > second and a[i] != first:
            second = a[i]
    if second == -2147483648:
        print("There is no second largest element")
    else:
        print("The second largest element is:", second)

a = list(map(int, input("Enter the elements of array: ").split()))
secondLargest(a, len(a))
