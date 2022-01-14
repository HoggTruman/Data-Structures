#python3
import sys
from math import inf

class StackWithMax():
    def __init__(self):
        self.stack = []
        self.maximum = -inf

    def Push(self, a):
        self.maximum = max(self.maximum, a)
        self.stack.append((a, self.maximum))

    def Pop(self):
        assert(len(self.stack))
        self.stack.pop()

    def Max(self):
        assert(len(self.stack))
        return self.stack[-1][1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
