def checkAnagrams(st1, st2):
    if len(st1) != len(st2):
        return False
    res = 0
    for i in range(0, len(st1)):
        res = res ^ ord(st1[i])
        res = res ^ ord(st2[i])
    return res == 0

s1, s2 = input("Enter the two strings to be checked for being anagrams: ").split()
if checkAnagrams(s1, s2):
    print("The given two strings are anagrams of each other")
else:
    print("The given two strings are not anagrams of each other")
