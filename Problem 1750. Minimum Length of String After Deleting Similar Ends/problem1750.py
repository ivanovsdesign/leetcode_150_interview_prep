'''
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).



Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

'''
from collections import deque

class Solution:
    def minimumLength(self, s: str) -> int:
        #dq = deque(s)
        left = 0
        right = len(s) - 1
        letters = []

        while left < right:
            print(letters)
            print(s[left:right])
            print(left, right)
            # checking if letters on left and right pointers are the same
            if s[left] == s[right]:
                letters.append(s[left])
                left += 1
                right -= 1
            elif letters and s[left] == letters[-1]:
                left += 1
            elif letters and s[right] == letters[-1]:
                right -= 1
            else:
                break

            if s[left:right + 1] == letters[-1]:
                return 0

        return len(s[left:right + 1])

solution = Solution()

s = "aabccabba"
s = "cabaabac"
s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
s = "abbbbbbbbbbbbbbbbbbba"

print(solution.minimumLength(s))
