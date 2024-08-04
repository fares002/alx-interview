#!/usr/bin/python3
"""N Queens puzzle solver"""
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(n):
    """Solve the N Queens puzzle and return all solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


def main():
    """Main function to handle input and print solutions"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
