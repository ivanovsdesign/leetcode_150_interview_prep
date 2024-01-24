from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def dfs(self, current, count, odd):
        if not current:
            return 0

        count[current.val] += 1
        odd_change = 1 if count[current.val] % 2 == 1 else -1
        odd += odd_change

        if not current.left and not current.right:
            res = 1 if odd <= 1 else 0
        else:
            res = self.dfs(current.left, count, odd) + self.dfs(current.right, count, odd)
        odd -= odd_change
        count[current.val] -= 1

        return res

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0
        return self.dfs(root, count, odd)
    
solution = Solution()

root = [2,3,1,3,1,None,1]

print(solution.pseudoPalindromicPaths(root))