from typing import List

'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # finding longest indices 
        lengths_array = []
        letters_dict = {}

        for element in arr:
            lengths_array.append(len(element))
            for letter in element: 
                letters_dict[letter] = 1

        return lengths_array, letters_dict
    

solution = Solution()

arr = ["un","iq","ue"]

print(solution.maxLength(arr))