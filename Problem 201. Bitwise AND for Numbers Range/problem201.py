'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        result = 0 

        for i in range(32):
            bit = (left >> i) & 1
            if not bit:
                continue

            remainder = left % (1 << (i + 1))
            difference = (1 << (i + 1)) - remainder
            if right - left < difference:
                result = result | (1 << i)
        
        return result


solution = Solution()

left, right = 5, 7

print(solution.rangeBitwiseAnd(left, right))