from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1:
            return 1
        
        trust_dict = defaultdict(int)

        for connection in trust:
            trust_dict[connection[1]] += 1
            trust_dict[connection[0]] -= 1

        for key, value in trust_dict.items():
            if value + 1 == n:
                return key
        
        return -1


solution = Solution()

n = 2
trust = [[1,2]]

print(solution.findJudge(n, trust))