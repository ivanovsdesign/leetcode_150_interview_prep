from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1

        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
                pointer -= 1
            else: 
                digits[pointer] += 1
                return digits
        return [1] + digits

solution = Solution()

digits = [4,3,2,1]
digits = [9,9]

print(solution.plusOne(digits))

