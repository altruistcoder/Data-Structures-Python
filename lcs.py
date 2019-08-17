def lcs(x, y):
    m = len(x)
    n = len(y)
    r = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                r[i][j] = 0
            elif x[i-1] == y[j-1]:
                r[i][j] = r[i-1][j-1] + 1
            else:
                r[i][j] = max(r[i - 1][j], r[i][j - 1])
    return r[m][n]

x, y = input("Enter the two strings: ").split()
print("The length of the longest common subsequence is: ", lcs(x, y))
