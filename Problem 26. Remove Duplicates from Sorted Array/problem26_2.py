from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_counter = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[unique_counter] = nums[i]
                unique_counter += 1
        return unique_counter
    
sol = Solution()

nums = [1,1,2]

print(sol.removeDuplicates(nums))