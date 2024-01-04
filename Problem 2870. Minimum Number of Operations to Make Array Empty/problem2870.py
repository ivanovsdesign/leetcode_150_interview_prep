import logging

logging.basicConfig(level=logging.DEBUG)


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fmap = []

        nums.sort()

        n = len(nums)
        search = []
        indeces = []
        k = 0

        for num in nums:
            logging.debug(f"External for cycle, num: {num}")
            search = []
            for i, nnum in enumerate(nums):
                logging.debug(f"Internal for cycle, num: {num}")
                logging.debug(f"Internal for cycle, num: {num} ; i: {i}; nums[i]: {nums[i]}; nnum: {nnum}")
                if nnum == num:
                     search.append(i)
            if len(search) == 2 or len(search) == 3:
                indeces.append(search)
        
        return indeces


sol = Solution()

nums = [2,3,3,2,2,4,2,3,4]

print(sol.minOperations(nums))