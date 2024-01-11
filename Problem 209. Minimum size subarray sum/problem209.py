from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l_pointer = 0
        r_pointer = len(nums)

        valid = []

        for l_pointer in range(len(nums)+1):
            for c in range(1, len(nums)+1):
                print(nums[l_pointer:c])
                if sum(nums[l_pointer:c]) >= target:
                    valid.append(len(nums[l_pointer:c]))

        try:
            return min(valid)
        except:
            return 0
        
sol = Solution()

target = 7
nums = [2,3,1,2,4,3]

print(sol.minSubArrayLen(target, nums))