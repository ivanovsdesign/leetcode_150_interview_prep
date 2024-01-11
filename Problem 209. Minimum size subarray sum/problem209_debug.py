from typing import List
import pdb

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l_pointer, temp = 0, 0

        result = float('inf')

        for r_pointer in range(len(nums)):
            temp += nums[r_pointer]

            # Set a breakpoint
            pdb.set_trace()

            while temp >= target:
                result = min(result, r_pointer - l_pointer + 1)
                temp -= nums[l_pointer]
                l_pointer += 1

        return 0 if result == float('inf') else result

# Example usage:
sol = Solution()
result = sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(result)
