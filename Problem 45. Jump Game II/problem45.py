'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''

from typing import List 
from collections import defaultdict

class Solution:
    def jump(self, nums: List[int]) -> int:

        nums_len_idx = len(nums) - 1
        current = -1
        next = 0
        jumps = 0
        i = 0

        while next < nums_len_idx:
            print(
                f'''
                current = {current}
                next = {next}
                jumps = {jumps}
                i = {i}
                '''
            )
            if i > current:
                jumps += 1
                current = next
            next = max(next, nums[i] + i)
            i += 1

        return jumps

solution = Solution()

nums = [2,3,0,1,4]
nums = [2,3,1,1,4]
#nums = [1]

print(solution.jump(nums))