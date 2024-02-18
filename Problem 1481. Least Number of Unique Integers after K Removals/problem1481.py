'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

'''

from typing import List
from collections import defaultdict
from 

class Solution:
    # Heapq solution



    # Sorting solution
    def findLeastNumOfUniqueIntsSorting(self, arr: List[int], k: int) -> int:
        arr.sort()

        number_dict = defaultdict(int)

        l,r = 0,len(arr)-1

        while l < r:
            number_dict[arr[l]] += 1
            number_dict[arr[r]] += 1
            l += 1
            r -= 1
        
        if len(arr) % 2 == 1:
            number_dict[arr[l]] += 1

        sorted_dict = dict(sorted(number_dict.items(), key = lambda x:x[1]))

        unique_nums = len(sorted_dict.keys())

        for key, value in sorted_dict.items():
            if k > 0:
                if value <= k:
                    k = k - value
                    print(value, k)
                    unique_nums -= 1
                else: 
                    break


        return unique_nums

solution = Solution()
arr = [5,5,4]
k = 1

arr = [4,3,1,1,3,3,2]
k = 3

print(solution.findLeastNumOfUniqueInts(arr, k))