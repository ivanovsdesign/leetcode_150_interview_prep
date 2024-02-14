'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
'''

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l = 0
            r = len(word) - 1
            if r == 0:
                return word
            while l < r:
                if word[l] != word[r]:
                    break
                if l + 1 == len(word) // 2:
                    return word
                l += 1
                r -= 1
        return ''
            
            

solution = Solution()

words = ["notapalindrome","google"]

word = 'racecar'

l = 0
r = len(word) - 1

while l < r:
    if word[l] != word[r]:
        break
    if l + 1 == len(word) // 2:
        print('palindrome')
    print(f'{word[l]} ::: {word[r]}\nl: {l}, r: {r}, mid: {len(word) // 2}')
    l += 1
    r -= 1

print(solution.firstPalindrome(words))