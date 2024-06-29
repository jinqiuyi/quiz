# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:00:45 2024

@author: JinQiuyi
"""

def reverse_list(l:list):
    l_reversed = [l[len(l)-i-1] for i in range(len(l))]
    return l_reversed

def solve_sudoku(matrix):
    row, col = find_empty_cell(matrix)

    if row == -1 and col == -1:
        return True

    for num in range(1, 10):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num

            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0
    return False

def find_empty_cell(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1

def is_valid(matrix, row, col, num):
    if num in matrix[row]:
        return False

    if num in [matrix[i][col] for i in range(9)]:
        return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    if num in [matrix[box_row + i][box_col + j] for i in range(3) for j in range(3)]:
        return False

    return True
