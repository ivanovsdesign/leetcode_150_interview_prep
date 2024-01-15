class Solution:
    def isValid(self, s: str) -> bool:
        
        pts = {'{':'}', '[':']', '(':')'}
        ptc = {'}':'{', ']':'[', ')':'('}

        stack = []

        for i in s:
            if i in pts.keys():
                stack.append(i)
            if i in pts.values():
                if not stack:
                    return False
                elif stack.pop() != ptc[i]:
                    return False
                else:
                    continue
            
        if not stack:
            return True
        else:
            return False

                    

            

    

sol = Solution()

s = "(){}"

print(sol.isValid(s))