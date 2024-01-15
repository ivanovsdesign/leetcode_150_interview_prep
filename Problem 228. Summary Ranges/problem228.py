from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        l = 0
        r = 0

        temp = []

        i = 1

        while i in range(1, len(nums)+1):
            l = nums[i-1]
            print(f'l:{l}')
            while i in range(1, len(nums)) and nums[i-1] == (nums[i] - 1):
                i += 1

            r = nums[i-1]

            if l == r:
                temp.append(str(l))
                print(f'r:{r}')
            else:
                temp.append(str(l) + '->' + str(r))
            i += 1
            
        return temp
           



sol = Solution()

nums = [0,1,2,4,5,7]

print(sol.summaryRanges(nums))


""" Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7" """