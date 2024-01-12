from typing import List
import numpy as np
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        segments = collections.defaultdict(set)
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == '.':
                    continue
                if (board[row][column] in rows[row] or
                    board[row][column] in columns[column] or
                    board[row][column] in segments[(row // 3, column // 3)]):
                    return False
                
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                segments[(row // 3, column // 3)].add(board[row][column])

        return True


        return len(board[0])



sol = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(sol.isValidSudoku(board))