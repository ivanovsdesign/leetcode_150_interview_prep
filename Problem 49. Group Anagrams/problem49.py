'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # alphabet characters

            for c in s:
                count[ord(c) - ord('a')] += 1

            print(s)

            result[tuple(count)].append(s)

        return result.values()
    
"""         result = []

        for i, word in enumerate(strs):
            if len(result) == 0 or word not in result[-1] and word != '-':
                temp_set = set(word)
                temp_arr = []
                temp_arr.append(word)
                for k in range(i+1, len(strs)):
                    if set(strs[k]) == temp_set:
                        temp_arr.append(strs[k])
                        strs[k] = '-'
                result.append(temp_arr)

        return result """



solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

strs = ["a"]

strs = [""]

strs = ["ddddddddddg","dgggggggggg"]

print(solution.groupAnagrams(strs))