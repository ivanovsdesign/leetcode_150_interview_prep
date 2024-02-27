'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                # checking escape condition
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        
        return ''
            
solution = Solution()

strs = ["flower","flow","flight"]

print(solution.longestCommonPrefix(strs))