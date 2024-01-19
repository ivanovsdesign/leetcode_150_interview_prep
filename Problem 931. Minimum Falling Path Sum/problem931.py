from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        row = 0
        col = 0
        sm = []

        # searching for the first element

        element = min(matrix[row])
        sm.append(element)
        col = matrix[row].index(element)
        row += 1

        

        # searching for the second element, minimal sum
        while row < len(matrix):
            if col > 0 and col < len(matrix[row]):
                boundaries = matrix[row][(col-1):(col+2)]
            elif col == 0:
                boundaries = matrix[row][col:(col+2)]
            else:
                boundaries = matrix[row][(col-1):col]
            
            if boundaries:
                element = min(boundaries)
                sm.append(element)
                col = matrix[row].index(element)
                row += 1
            else:
                break 
        
        return sum(sm)
        
        
solution = Solution()

matrix = [[-19,57],[-40,-5]]
#matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-80,-13,22],[83,94,-5],[73,-48,61]]
matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]

print(solution.minFallingPathSum(matrix))