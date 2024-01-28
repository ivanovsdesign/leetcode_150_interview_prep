from typing import List
from collections import defaultdict

'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0
'''

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        print(f'ROWS: {ROWS}, COLS: {COLS}')

        sub_sum = [[0] * COLS for _ in range(ROWS)]
        print(f'sub_sum: {sub_sum}')

        for r in range(ROWS):
            for c in range(COLS):
                top = sub_sum[r-1][c] if r > 0 else 0
                left = sub_sum[r][c-1] if c > 0 else 0
                top_left = sub_sum[r-1][c-1] if min(r,c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        print(sub_sum)

        res = 0

        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = defaultdict(int) # prefix_sum -> count
                count[0] = 1
                for c in range(COLS):
                    cur_sum = sub_sum[r2][c] - (
                        sub_sum[r1-1][c] if r1 > 0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1


        return res

solution = Solution()

matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0

print(solution.numSubmatrixSumTarget(matrix, target))