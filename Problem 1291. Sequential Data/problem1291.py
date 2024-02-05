'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
'''

from typing import List
from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        sequence = deque(range(1,10))
        result = []

        while sequence: 
            n = sequence.popleft()
            if n > high:
                continue
            if low <= n <= high:
                result.append(n)
            ones = n % 10
            if ones < 9:
                sequence.append(n * 10 + (ones+1))

        return result
        

solution = Solution()

low = 1000
high = 13000

print(solution.sequentialDigits(low, high))