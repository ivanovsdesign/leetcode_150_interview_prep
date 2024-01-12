class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        n = 0
        counter = 0

        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        for l in ransomNote:
            for i in range(n, len(magazine)): 
                if l == magazine[i]:
                    magazine[i] = '_'
                    counter += 1
                    break
            n = i
        
        return ransomNote, magazine, len(ransomNote) == counter

sol = Solution()

ransomNote = "ab"
magazine = "aabaa"

ransomNote = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"

print(sol.canConstruct(ransomNote, magazine))