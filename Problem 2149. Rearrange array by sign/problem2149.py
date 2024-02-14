'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
'''

from typing import List
from collections import deque

class Solution:
    def rearrangeArrayTheDumbWay(self, nums: List[int]) -> List[int]:

        # Setting the starting element as positive
        if nums[0] < 0:
            for i, num in enumerate(nums):
                if num > 0:
                    nums[i] = nums[0]
                    nums[0] = num 
                    break

        for i in range(1, len(nums)):
            if nums[i-1] < 0:
                if nums[i] < 0:
                    continue
                elif nums[i] > 0:
                    continue
            if nums[i-1] > 0:
                if nums[i] < 0:
                    continue
                if nums[i] > 0:
                    for k in range(i, len(nums)):
                        if nums[k] < 0:
                            temp = nums[i]
                            nums[i] = nums[k]
                            nums[k] = temp
        return nums

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Getting positive numbers
        positive = deque()
        negative = deque()

        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                positive.append(nums[i-1])
            else: 
                negative.append(nums[i-1])
        
        i = 0 
        
        while i * 2 < len(nums):
            nums[i * 2] = positive[i]
            nums[i * 2 + 1] = negative[i]
            i += 1
                



        return nums

solution = Solution()

nums = [3,1,-2,-5,2,-4]

nums = [-1,1]

nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]

print(solution.rearrangeArray(nums))