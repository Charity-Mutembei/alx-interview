#!/usr/bin/env python3
"""
NQueen task
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if there is a queen in the same row on the left
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """
    Check if there is a queen in the upper diagonal on the left
    """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """
    Check if there is a queen in the lower diagonal on the left
    """
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n):
    """
    solve queens
    """
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n)
            board[i][col] = 0


def solve_nqueens(n):
    """
    secondd
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens_util(board, 0, n)


def print_solution(board):
    """
    print
    """
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
