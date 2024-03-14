'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
'''

from typing import List 

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count_dict = {0: 1}
        subarray_sum = 0
        result = 0

        for num in nums: 
            subarray_sum += num 
            if subarray_sum - goal in count_dict:
                result += count_dict[subarray_sum - goal]
            count_dict[subarray_sum] = count_dict.get(subarray_sum, 0) + 1

        return result
                
    
    def numSubarraysWithSumNaive(self, nums: List[int], goal: int) -> int:
        result = 0

        subarray_sum = 0

        left_pointer = 0
        right_pointer = 0

        
        subarray_sum += nums[left_pointer]
        while right_pointer < len(nums):
            subarray_sum += nums[right_pointer]
            right_pointer += 1
            if subarray_sum == goal: 
                result += 1
            print(nums[left_pointer:right_pointer])
        
        while left_pointer < right_pointer:
            subarray_sum -= nums[left_pointer]
            left_pointer += 1
            if subarray_sum == goal:
                result += 1
            print(nums[left_pointer:right_pointer])
            
    
        return result 
    
solution = Solution()

nums = [1,0,1,0,1]
goal = 2

nums = [0,0,0,0,0]
goal = 0

print(solution.numSubarraysWithSum(nums, goal))