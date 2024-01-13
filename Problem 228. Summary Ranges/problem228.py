from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a = 0
        b = 0

        temp = set()
        ta = []

        for b in range(1, len(nums)):
            if nums[b] == (nums[b-1] + 1):
                temp.add(nums[b-1])
                temp.add(nums[b])
            if nums[b] != (nums[b-1] + 1):
                ta.append(temp)
                ta.append({nums[b]})
                temp = set()
           

        return ta


sol = Solution()

nums = [0,1,2,4,5,7]

print(sol.summaryRanges(nums))


""" Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7" """