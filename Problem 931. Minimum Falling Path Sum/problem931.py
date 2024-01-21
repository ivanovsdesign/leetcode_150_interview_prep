from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        # Create a copy of the matrix to store intermediate results
        dp = [[0] * cols for _ in range(rows)]
        dp[0] = matrix[0]  # The first row is the same as the input matrix

        # Iterate through the matrix starting from the second row
        for i in range(1, rows):
            for j in range(cols):
                # Find the minimum sum from the previous row considering adjacent elements
                dp[i][j] = matrix[i][j] + min(dp[i-1][max(0, j-1):min(cols, j+2)])

        # The result is the minimum value in the last row
        return min(dp[-1])


        
        
solution = Solution()

matrix = [[-19,57],[-40,-5]]
#matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-80,-13,22],[83,94,-5],[73,-48,61]]
matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]

print(solution.minFallingPathSum(matrix))