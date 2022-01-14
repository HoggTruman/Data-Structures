# python3

class Heap():
    def __init__(self, data, n):
        self.heap = data
        self.size = n
        self.swaps = []

    def parent(self, i):
        return i//2

    def left_child(self, i):
        return 2*i

    def right_child(self, i):
        return 2*i+1

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= self.size and self.heap[l] < self.heap[min_index]:
            min_index = l
        r = self.right_child(i)
        if r <= self.size and self.heap[r] < self.heap[min_index]:
            min_index = r
        if i != min_index:
            self.swaps.append((i-1, min_index-1))
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index)

    def build_heap_fast(self):
        self.heap = [0] + self.heap
        for i in range(self.size//2, 0, -1):
            self.sift_down(i)
        return self.swaps




def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    CaseHeap = Heap(data,n)
    swaps = CaseHeap.build_heap_fast()

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
