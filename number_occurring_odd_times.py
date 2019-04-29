def getOddOccurrences(a):
    r = 0
    for i in a:
        # XORing with the previous result in every iteration
        r = r ^ i
    return r


a = list(map(int, input("Enter a list of elements: ").split()))
o = getOddOccurrences(a)
print("Number occurring odd no. of times in the given array is", o)
