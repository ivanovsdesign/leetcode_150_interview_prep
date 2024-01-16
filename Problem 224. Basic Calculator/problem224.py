class Solution:
    def find_num(self, s: str):
        num = ''
        stop = 0
        for i, k in enumerate(s):
            if k.isdigit():
                num += k
                stop = i+1

        return int(num), s[stop:]
    
    def find_sign(self, s):
        for i in s:
            if i in ['+', '-']:
                if i == '+':
                    return 1
                if i == '-': return -1

    def calculate(self, s: str) -> int:
        l, next = self.find_num(s)
        r, _ = self.find_num(next)
        result = l + self.find_sign(next) * r


        return result

    
s = "21 + 2"

solution = Solution()

print(solution.calculate(s))