class Solution:
    def isValid(self, s: str) -> bool:
        
        pts = {'{':'}', '[':']', '(':')'}

        i = 0
        n = len(s) - 1

        while i <= n:
            if pts[s[i]] == s[n]:
                i += 1
                n -= 1
            else:
                return False

        return True
            

    

sol = Solution()

s = "(]"

print(sol.isValid(s))