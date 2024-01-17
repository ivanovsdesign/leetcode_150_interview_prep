class Solution:
    def find_num(self, s: str):
        i = 0
        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        
        return (int(num), s[i:]) if num else (0, s)
        
    def find_sign(self, s: str):
        i = 0

        while i < len(s) and s[i] not in ['+', '-', '(', ')']:
            i += 1
        
        if i < len(s):
            if s[i] == '+':
                return '+', s[(i+1):]
            elif s[i] == '-':
                return '-', s[(i+1):]
            elif s[i] == '(':
                return '(', s[(i+1):]
            elif s[i] == ')':
                return ')', s[(i+1):]

        return '+', s

    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append((result, sign))
                result, sign = 0, 1
            elif char == ')':
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        return result + sign * num

    
s = "(21 - 2) + 1"

solution = Solution()
print(solution.calculate(s))

#print(solution.calculate(s))