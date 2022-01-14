# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;

    def construct_tree(self):
        self.tree = [[] for i in range(self.n)]
        for i in range(self.n):
            if self.parent[i] > -1:
                self.tree[self.parent[i]].append(i)
            else:
                self.root_index = i

    def compute_height_fast(self):
        queue = []
        height = 1
        for i in self.tree[self.root_index]:
                queue.append((i, 2))
        while queue:
                current_index = queue[0][0]
                for i in self.tree[current_index]:
                    queue.append((i, queue[0][1] + 1))
                height = max(height, queue.pop(0)[1])


        return height



def main():
    casetree = Tree()
    casetree.read()
    casetree.construct_tree()
    print(casetree.compute_height_fast())


threading.Thread(target=main).start()
