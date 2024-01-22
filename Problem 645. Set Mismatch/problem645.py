from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else: 
                nums[abs(num) - 1] *= -1
        
        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i+1]


    
solution = Solution()

nums = [1,2,2,4]
#nums = [1,1]
#nums = [3,2,2]

print(solution.findErrorNums(nums))