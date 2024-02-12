
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)

        while l < r:
            
            center = (l + r) // 2

            if target >= nums[center]:
                l = center + 1
            else:
                r = center
        
        if target == nums[l - 1] and l > 0:
            return l - 1
        else: 
            return -1


solution = Solution()

nums = [-1,0,3,5,9,12]
target = 2

print(solution.search(nums, target))