#!/usr/bin/python3
"""
Task 0: Rorate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything.
    The matrix must be edited in-place.
    You can assume the matrix will have 2
    dimensions and will not be empty.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
