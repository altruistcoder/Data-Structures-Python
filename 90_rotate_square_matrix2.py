def reverseColumns(a, R, C):
    for i in range(C):
        j = 0
        k = C - 1
        while j < k:
            t = a[j][i]
            a[j][i] = a[k][i]
            a[k][i] = t
            j += 1
            k -= 1


def matrixTranspose(a, R, C):
    for i in range(R):
        for j in range(i, C):
            t = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = t


def displayMatrix(a, R, C):
    for i in range(R):
        for j in range(C):
            print(str(a[i][j]), end=" ")
        print()


# Function to anticlockwise rotate matrix by 90 degree
def rotateMatrix90(a, R, C):
    matrixTranspose(a, R, C)
    reverseColumns(a, R, C)


R = int(input("Enter the no. of rows of the matrix: "))
C = int(input("Enter the no. of columns of the matrix: "))
a = []
print("Enter the elements of the matrix: ")
for i in range(R):
    a.append(list(map(int, input().split())))

print("Original Array: ")
displayMatrix(a, R, C)
print("90 Degrees Rotated Array:")
rotateMatrix90(a, R, C)
displayMatrix(a, R, C)
