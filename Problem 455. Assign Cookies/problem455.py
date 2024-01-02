class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        s.sort()
        g.sort()

        i = k = 0

        while i < len(g) and k < len(s):
            if g[i] <= s[k]:
                i += 1
                k += 1
            else:
                k += 1

        return i