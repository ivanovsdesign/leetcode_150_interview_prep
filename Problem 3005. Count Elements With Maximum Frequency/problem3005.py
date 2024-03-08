'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.



Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
'''
from collections import defaultdict
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count_dict = defaultdict(int)
        max_count = 0
        occurencies_count = 0

        for num in nums:
            count_dict[num] += 1
            frequency = count_dict[num]
            #max_count = max(max_count, count_dict[num])

            if frequency > max_count:
                max_count = frequency
                occurencies_count = frequency
            elif frequency == max_count:
                occurencies_count += frequency

        return occurencies_count

solution = Solution()

nums = [1,2,2,3,1,4]

print(solution.maxFrequencyElements(nums))
