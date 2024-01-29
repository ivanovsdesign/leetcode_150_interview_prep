from collections import deque

class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        print(self.stack)

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.push(self.stack.pop())
        return self.stack.popleft()

    def peek(self) -> int:
        result = self.stack[0]
        print(result)
        return result

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
        
obj = MyQueue()

stack = deque()

'''
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]
'''

obj.push(1)
obj.push(2)

obj.peek()

print(obj.pop())

obj.peek()