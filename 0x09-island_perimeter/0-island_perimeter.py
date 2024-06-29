#!/usr/bin/python3
"""
Module for the class Square
"""


def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Found land
                # Check its 4 neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0:
                        perimeter += 1
                    if nr >= rows:
                        perimeter += 1
                    if nc < 0:
                        perimeter += 1
                    if nc >= cols:
                        perimeter += 1
                    if grid[nr][nc] == 0:
                        perimeter += 1

    return perimeter
