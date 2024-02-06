'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dictionary = defaultdict(int)

        for i in s:
            dictionary[i] += 1
        
        key = [k for k, v in dictionary.items() if v == 1]

        return s.index(key[0]) if key else -1
    
solution = Solution()

s = "llmm"

print(solution.firstUniqChar(s))