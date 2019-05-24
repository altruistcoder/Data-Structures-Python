NO_OF_CHARS = 256

# This function returns the first non-repeating character in the given array.
# If there is no non-repeating character then it returns -1
def firstNonRepeating(s):
    f = [0] * NO_OF_CHARS
    for i in s:
        f[ord(i)] += 1
    for i in range(len(s)):
        if f[ord(s[i])] == 1:
            return i
    return -1


s = input("Enter a String: ")
r = firstNonRepeating(s)
if r == -1:
    print("No non-repeating character present in the given string. Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is " + s[r])
