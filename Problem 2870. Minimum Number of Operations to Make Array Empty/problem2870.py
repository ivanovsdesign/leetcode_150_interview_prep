import logging

logging.basicConfig(level=logging.DEBUG)


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        logging.debug(f"nums_sorted: {nums}")

        search = []
        indeces = []
        takes = 0
        current_num = 0

        for num in nums:
            logging.debug(f"External for cycle, num: {num}")


            if num != current_num:
                for i, nnum in enumerate(nums):
                    logging.debug(f"Internal for cycle, num: {num}")
                    logging.debug(f"Internal for cycle, num: {num} ; i: {i}; nums[i]: {nums[i]}; nnum: {nnum}")
                    if nnum == num:
                        search.append(i)
                if len(search) % 2 == 0 or len(search) % 3 == 0:
                    indeces.append(search)
                    current_num = num
            
            search = []

        search = []

        for idxs in indeces:
            for idx in idxs:
                search.append(idx)

        if len(search) == len(nums):
            for idxs in indeces:
                logging.debug(f"idxs len: {len(idxs)}")
                if len(idxs) % 2 == 0:
                    logging.debug(f"idxs % 2: {len(idxs) / 2}")
                    takes += int((len(idxs) / 2))
                elif len(idxs) % 3 == 0:
                    logging.debug(f"idxs % 3: {len(idxs) / 3}")
                    takes += int((len(idxs) / 3))
            for i in sorted(search, reverse=True):
                del nums[i]
        else:
            takes = -1

        logging.debug(f"nums: {nums}")
        logging.debug(f"search: {search}")
        logging.debug(f"indeces: {indeces}")

        return takes


sol = Solution()

nums = [2,3,3,2,2,4,2,3,4]
#nums = [2,1,2,2,3,3]
nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]

print(sol.minOperations(nums))