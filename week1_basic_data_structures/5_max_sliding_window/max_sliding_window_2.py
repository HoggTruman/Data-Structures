# python3
import sys
from math import inf


def max_sliding_window(sequence, m):
    queue = []
    max_store = []
    for i in range(len(sequence)):
        while queue and sequence[queue[-1]] <= sequence[i]:
            queue.pop()
        queue.append(i)
        if i >= m-1:
            if i-m+1 <= queue[0] <= i:
                max_store.append(sequence[queue[0]])
            else:
                queue.pop(0)
                max_store.append(sequence[queue[0]])

    return max_store


if __name__ == '__main__':
    n = int(input())
    sequence = [int(i) for i in input().split()]
    assert len(sequence) == n
    m = int(input())
    print(*max_sliding_window(sequence, m))