'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            median = len(nums) // 2
            left, right = merge_sort(nums[:median]), merge_sort(nums[median:])
            return merge(left, right)

        def merge(left, right):
            result = []
            while (left and right):
                if left[0] < right[0]:
                    result.append(left[0])
                    left.pop(0)
                else: 
                    result.append(right[0])
                    right.pop(0)
            
            if left:
                result += left
            if right: 
                result += right
            
            return result

        

        return merge_sort(nums)
    
    def missingNumberArithmetic(self, nums: List[int]) -> int:

        n = max(nums) + 1
        #max_num = max(nums)
        a = min(nums)
        d = 1
        
        arithmetic_progression_sum = (n/2)*(2*a + (n-1)*d)

        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1
        
        print(f'diff: {arithmetic_progression_sum}')
            
        if arithmetic_progression_sum - sum(nums) > 0:
            return int(arithmetic_progression_sum - sum(nums))
        else: 
            if a == 0:
                return int(n)
            else:
                return 0

    def missingNumberSlow(self, nums: List[int]) -> int:
        max_num, min_num, num_sum = 0, 0, 0

        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            num_sum += num

        num_set = set(range(min_num, max_num+1))

        if len(num_set - set(nums)) == 0:
            return max_num + 1
        else: 
            return (num_set - set(nums)).pop()

solution = Solution()

nums = [1,2]

print(solution.missingNumberArithmetic(nums))