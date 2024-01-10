from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r in range(0, len(nums)):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                count += 1
                r += 1
    
            for _ in range(min(2, count)):
                if l < len(nums):
                    nums[l] = nums[r]
                    l += 1
            r += 1  
        
                
        return l
    
sol = Solution()

nums = [1,1,1,2,2,3]

print(sol.removeDuplicates(nums))