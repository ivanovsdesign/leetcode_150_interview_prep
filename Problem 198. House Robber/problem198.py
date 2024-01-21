from typing import List
import numpy as np

'''
    nums = [1,2,3,4,5,6,7,8]

            [1]
        [3]     [4]
[5][6][7][8]    [6][7][8]
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        left, right = 0, 0

        for num in nums:
            first = max(left + num, right)
            left = right
            right = first

        return first


solution = Solution()

nums = [1,2,3,1]

print(solution.rob(nums))

