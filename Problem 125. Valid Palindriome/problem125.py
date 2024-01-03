import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s)
        s = s.lower()
        
        i = 0
        n = len(s) - 1

        result = True

        for i in range(n + 1):
            while i < (n - i):
                if s[i] != s[n - i]:
                    result = False
                    break
                i += 1
        
        return result

sol = Solution()

s = "ab_a"

print(sol.isPalindrome(s))