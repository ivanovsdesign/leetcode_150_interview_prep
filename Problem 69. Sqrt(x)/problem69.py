class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Approximation:
        (y-n)^2 = 0
        (x - 2ny + n^2) = 0
        n = 2y - x/n
        '''

        if x < 2:
            return x
        else: 
            y = x
            n = (y + (x/y)) / 2

            while abs(y-n) >= 0.001:
                y = n
                n = (y + (x/y)) / 2
            
            return int(n)


solution = Solution()

x = 4

print(solution.mySqrt(x))