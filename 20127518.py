#!/usr/bin/env python
# coding: utf-8

#20127518
#Nguyen Quoc Huy

# In[1]:

import copy

def swapRow(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k


def nulScalar(A, r, k):
    size = len(A[r])
    for m in range(0, size):
        A[r][m] *= k


def addRow(A, r1, k, r2):
    size = len(A[0])
    for i in range(0, size):
        A[r1][i] += k * A[r2][i]


def createIdentityMatrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def printMatrix(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] == 0.0:
                print(abs(A[i][j]), end=" ")
            else:
                print(A[i][j], end=" ")

        print("")
    print("")

def pivoting(A, pRow, pCol):
    n = len(A)
    for i in range(pRow, n):
        if A[i][pCol] != 0:
            nulScalar(A, i, 1 / A[i][pCol])
            swapRow(A, pRow, i)

            #find remaining rows to perform addRow
            for j in range(0, n):
                if pRow == j:
                    continue
                addRow(A, j, -A[j][pCol], pRow)

            return 1
    return 0

# def Gauss_elimination(A):
#     i, j = 0, 0
#     n = len(A)
#     m = len(A[0])
#     while i < n:
#         if pivoting(A, i, j):
#             i += 1
#         j += 1
#         if j == m - 1:
#             return

#Transform into Echelon Form
def changeMatrixToEchelon(A, pRow, pCol):
    for i in range(pRow, len(A)):
        if A[i][pCol] != 0:
            # find leader in matrix
            nulScalar(A, i, 1 / A[i][pCol])
            swapRow(A, pRow, i)

            # change
            for j in range(0, len(A)):
                if pRow == j:
                    continue
                addRow(A, j, -A[j][pCol], pRow)

            return 1
    return 0


def createSubmatrix(A, iRow, iCol):

    subA = copy.deepcopy(A)
    # Remove row
    subA = subA[:iRow] + subA[iRow + 1:]

    # Remove col
    n_row_sub = len(subA)
    for i in range(n_row_sub):
        subA[i] = subA[i][:iCol] + subA[i][iCol + 1:]

    return subA


# Solve square matrix
#Find deterninant of matrix
def solveDeterminant(A):

    row = len(A)
    col = len(A[0])

    # if the matrix has 1 row 1 col
    if row == 1 and col == 1:
        return A[0][0]

    # Go through each column to remove
    total = 0
    for iCol in range(col):
        subA = createSubmatrix(A, 0, iCol)
        # Find sign
        sign = (-1) ** (iCol % 2)

        # Recursively calling for submatrix
        subDet = solveDeterminant(subA)

        # Factor accumulation when removing column iCol
        total += sign * A[0][iCol] * subDet

    return total

def inverse(A):
    if solveDeterminant(A) == 0:
        print("Matrix can not inverse", end="")
        return

    size = len(A)

    newSize = size * 2

    subCol = 0
    newMatrix = []

    # create a matrix that is combined with identity matrix
    for i in range(size):
        temp = []
        for j in range(newSize):
            if j < size:
                temp.append(A[i][j])
            else:
                if j >= size and size + subCol == j:
                    temp.append(1)
                else:
                    temp.append(0)
        subCol += 1
        newMatrix.append(temp)

    print("Matrix (A|I):")
    printMatrix(newMatrix)

    i = 0
    j = 0
    while i < size:
        if changeMatrixToEchelon(newMatrix, i, j):
            i += 1
        j += 1
        if j == size:
            break

    print("After processing: ")
    printMatrix(newMatrix)
    print("")

    result = []

    for i in range(size):
        tempArr = []
        for j in range(size, newSize):
            temp = newMatrix[i][j]
            tempArr.append(temp)
        result.append(tempArr)

    print("Inverse matrix: ")
    printMatrix(result)

# Solve problem

if __name__ == "__main__":
    A = [[1, 2, 1], [3, 7, 3], [2, 3, 4]]
    print("Exercise 1: ")
    inverse(A)

    B = [[1, -1, 2], [1, 1, -2], [1, 1, 4]]
    print("Exercise 2: ")
    inverse(B)

    C = [[1, 2, 3], [2, 5, 3], [1, 0, 8]]
    print("Exercise 3: ")
    inverse(C)

    D = [[-1, 3, -4], [2, 4, 1], [-4, 2, -9]]
    print("Exercise 4: ")
    inverse(D)


