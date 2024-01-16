class Solution:
    def find_num(self, s: str):
        i = 0
        num = ''
        if s[i].isdigit():
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
        
        return (int(num), s[i:])  if num else (0,s)
        
    def find_sign(self, s: str):
        i = 0

        while i < len(s) and s[i] not in ['+', '-']:
            i += 1
        
        if s[i] == '+':
            return 1, s[(i+1):]
        if s[i] == '-':
            return -1, s[(i+1):]
        

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        l, nxt = self.find_num(s)
        print(f'l:{l}, next:{nxt}')
        sign, nxt = self.find_sign(nxt)
        print(f'sign:{sign}, next:{nxt}')
        r, nxt = self.find_num(nxt)
        print(f'r:{r}, next:{nxt}')
        result = l + (r * sign)

        return result

    
s = "21 - 2"

solution = Solution()
print(solution.calculate(s))

#print(solution.calculate(s))