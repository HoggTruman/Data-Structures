# python3
import sys
from math import inf


class StackWithMax():
    def __init__(self):
        self.stack = []
        self.maximum = -inf

    def Push(self, a):
        self.maximum = max(self.maximum, a)
        self.stack.append((a, self.maximum))

    def Pop_Bottom(self):
        return self.stack.pop(0)[0]

    def Pop_Top(self):
        return self.stack.pop()[0]

    def Max(self):
        return self.stack[-1][1]

def max_sliding_window(sequence, m):
    max_store = []
    stack1 = StackWithMax()
    stack2 = StackWithMax()
    for i in range(m):
        stack1.Push(sequence.pop(0))
    max_store.append(stack1.Max())

    while sequence:
        stack1.Pop_Bottom()
        for i in range(m-1):
            stack2.Push(stack1.Pop_Bottom())
        stack2.Push(sequence.pop(0))
        max_store.append(stack2.Max())
        stack1 = stack2
        stack2 = StackWithMax()

    return max_store


if __name__ == '__main__':
    n = int(input())
    sequence = [int(i) for i in input().split()]
    assert len(sequence) == n
    m = int(input())
    print(*max_sliding_window(sequence, m))

