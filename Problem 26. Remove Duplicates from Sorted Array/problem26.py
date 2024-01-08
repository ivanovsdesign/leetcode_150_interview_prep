from typing import List

class Solution:
    def check_numeric(self, val):
        try:
            return int(val)
        except:
            return float('inf')
        
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        for i, num in enumerate(nums):
            if (i+1) < len(nums):
                if nums[i+1] == num:
                    nums[i] = None
                    counter += 1
        
        unique_counter = len(nums) - counter

        #nums = [x for x in nums if x not in ['_']]
        
        nums = sorted(nums, key=self.check_numeric)
        return unique_counter
    
sol = Solution()

nums = [1,1,2]

print(sol.removeDuplicates(nums))