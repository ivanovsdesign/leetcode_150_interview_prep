class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        start = 0
        temp = 0
        counter = 0

        for l in range(len(s)):
            for r in range(start, len(t)):
                if s[l] == t[r]:
                    counter += 1
                    temp = r
                    break
            if counter >= 1:
                start = temp + 1
            else:
                return False
                
        
        return counter == len(s)

sol = Solution()

s = "abc"
t = "ahbgdc"

s = "bb"
t = "ahbgdc"

s = "acb"
t = "ahbgdc"

s = "abc"
t = "ahbgdc"


print(sol.isSubsequence(s,t))