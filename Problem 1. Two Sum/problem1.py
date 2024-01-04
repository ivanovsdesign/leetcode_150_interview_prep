class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        pair = []

        i = 0
        n = len(nums) - 1
        while i < (n + 1) and (n - i) > 0:
            print(nums[i] + nums[n - i])
            if nums[i] + nums[n - i] == target:
                pair = [i, n-i]
            i += 1
        
        return pair
    

sol = Solution()

nums = [2,7,11,15]
target = 9

print(sol.twoSum(nums, target))