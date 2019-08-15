def binaryPalindrome(num):
    rev = 0
    n1 = num
    while n1 > 0:
        rev <<= 1
        if (n1 & 1) == 1:
            rev ^= 1
        n1 >>= 1
    return num == rev

n = int(input("Enter a number: "))
if binaryPalindrome(n):
    print("The given number's binary representation is palindrome")
else:
    print("The given number's binary representation is not palindrome")
