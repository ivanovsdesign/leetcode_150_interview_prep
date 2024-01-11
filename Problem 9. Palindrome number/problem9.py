import numpy as np

class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        rev = 0

        while orig > 0:
            digit = orig % 10
            print(f'digit: {digit}')
            rev = rev * 10 + digit
            print(f'rev: {rev}')
            orig //= 10
            print(f'orig: {orig}')
        
        return x == rev
    

sol = Solution()

x = 121

print(sol.isPalindrome(x))