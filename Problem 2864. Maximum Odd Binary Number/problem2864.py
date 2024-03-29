'''
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

 

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
'''
from collections import deque

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        s = [c for c in s]
        left = 0

        for i in range(len(s)):
            if s[i] == '1':
                s[i], s[left] = s[left], s[i]
                left += 1
        s[left - 1], s[len(s) - 1] = s[len(s) - 1], s[left-1]

        return ''.join(s)


    
    def maximumOddBinaryNumberNaive(self, s: str) -> str:
    
        ones = []
        one = '0'
        zeros = []

        for i in s:
            if i == '1' and one == '0':
                one = '1'
                continue
            if i == '1' and one == '1':
                ones.append(i)
            if i == '0':
                zeros.append(i)
                

        return ''.join(ones + zeros + [one])

solution = Solution()

s = "010"
s = "0101"

print(solution.maximumOddBinaryNumber(s))