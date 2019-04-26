def findPair(a, n, s):
    # Creating an empty hash set
    h = set()

    for i in range(0, n):
        temp = s - a[i]
        if temp >= 0 and temp in h:
            print("Pair with the given sum is", temp, "and", a[i])
        h.add(a[i])
    print(h)


a = list(map(int, input("Enter the values of the array: ").split()))
s = int(input("Enter the value of sum to be find: "))
findPair(a, len(a), s)