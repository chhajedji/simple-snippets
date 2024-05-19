#!/usr/bin/env python3

# https://leetcode.com/problems/valid-sudoku

class Solution:

    def all_good(self, arr: list) -> bool:
        nums = []
        for n in arr:
            if n != '.':
                nums.append(n)

            if (len(nums) != len(set(nums))):
                return False

        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for row in board:
            if not (self.all_good(row)):
                return False

        clm = [[] for _ in range(9)]

        for i in range(9):
            clm[i] = [board[j][i] for j in range(9)]

        for row in clm:
            if not (self.all_good(row)):
                return False

        box = []

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                row = []
                for k in range(3):
                    row.append(board[i+k][j])
                    row.append(board[i+k][j+1])
                    row.append(board[i+k][j+2])

                if not (self.all_good(row)):
                    return False

        return True

obj = Solution()

board = \
[["5","3",".",  ".","7",".",    ".",".","."]
,["6",".",".",  "1","9","5",    ".",".","."]
,[".","9","8",  ".",".",".",    ".","6","."]

,["8",".",".",  ".","6",".",    ".",".","3"]
,["4",".",".",  "8",".","3",    ".",".","1"]
,["7",".",".",  ".","2",".",    ".",".","6"]

,[".","6",".",  ".","8",".",    "2","8","."]
,[".",".",".",  "4","1","9",    ".",".","5"]
,[".",".",".",  ".","8",".",    ".","7","9"]]

print(obj.isValidSudoku(board))
