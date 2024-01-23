from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}

        for num in set(nums):
            freq[num] = 0
        
        for num in nums:
            freq[num] += 1

        result = [key for key,value in freq.items() if value >= len(nums)/2]

        return result[0]
    
solution = Solution()

nums = [3,2,3]

print(solution.majorityElement(nums))