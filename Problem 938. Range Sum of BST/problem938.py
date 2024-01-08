""" Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32. """


from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root: TreeNode, low, high) -> int:
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        return (
            root.val +
            self.rangeSumBST(root.left, low, high) +
            self.rangeSumBST(root.right, low, high)
        )
    
root = [10,5,15,3,7,None,18]
low = 7
high = 15

sol = Solution()

print(sol.rangeSumBST(root, low, high))