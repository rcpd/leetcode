"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.
"""
from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        board_dict = {}

        # scan the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell in board_dict:
                    board_dict[cell].append((i, j))
                else:
                    board_dict[cell] = [(i, j)]

        # TODO: could do this while scanning
        for char in word:
            if char not in board_dict:
                return False

        visited = []
        k = 0
        for k, char in enumerate(word):
            # loop until a link is found or all possibilities exhausted
            while board_dict[word[k]]:
                # extract a new coord
                coord = board_dict[word[k]][-1]

                # if not visited and not last char
                if k < len(word)-1:
                    # test if next char has any unvisited links to current char
                    for coord2 in board_dict[word[k+1]]:
                        # if char and next char aligned on column or row
                        if ((coord[0] == coord2[0]-1 or coord[0] == coord2[0]+1) and coord[1] == coord2[1]) or \
                                ((coord[1] == coord2[1]-1 or coord[1] == coord2[1]+1) and coord[0] == coord2[0]):
                            if coord not in visited:
                                visited.append(coord)
                                print(coord)
                                print()
                            if coord2 not in visited:
                                visited.append(coord2)
                                print(coord2)
                                print()

                        # found a link for coord/coord2, break to avoid duplication
                        if len(visited) > k+1:
                            break

                # if no link found, backtrack and try again
                if len(visited) <= k:
                    board_dict[word[k]].pop()
                    if visited:
                        visited.pop()
                else:
                    # if link found, allow outer loop to advance to next char
                    break


        if len(visited) > k:
            print(True)
            return True
        else:
            print(False)
            return False

# test code
# assert Solution.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED")
assert Solution.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="SEE")
# assert not Solution.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB")
