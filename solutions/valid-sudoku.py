"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List


class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            # check row
            row_cells=[]
            for cell in row:
                if cell == ".":
                    continue

                if cell not in row_cells:
                    row_cells.append(cell)
                else:
                    return False

            # check column
            column_cells = []  # redundant
            for j in range(len(board)):
                cell = board[j][i]
                if cell == ".":
                    continue

                if cell not in column_cells:
                    column_cells.append(cell)
                else:
                    return False

        # check square
        # "outer" squares
        for o_row in range(3):
            for o_col in range(3):
                # "inner" squares
                square_cells = []
                for i_row in range(3):
                    for i_col in range(3):
                        actual_row = i_row + (3 * o_row)
                        actual_col = i_col + (3 * o_col)
                        cell = board[actual_col][actual_row]

                        if cell == ".":
                            continue

                        if cell not in square_cells:
                            square_cells.append(cell)
                            print(square_cells)
                        else:
                            return False

        return True


# test code
assert Solution.isValidSudoku(board=
                              [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                               [".", "9", "8", ".", ".", ".", ".", "6", "."],
                               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                               [".", "6", ".", ".", ".", ".", "2", "8", "."],
                               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True

assert Solution.isValidSudoku(board=
                              [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                               [".", "9", "8", ".", ".", ".", ".", "6", "."],
                               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                               [".", "6", ".", ".", ".", ".", "2", "8", "."],
                               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False

