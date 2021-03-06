# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c



    def inOrder(self,i):
        if i == 0:
            self.result = []

        if self.left[i] != -1:
            self.inOrder(self.left[i])

        self.result.append(self.key[i])

        if self.right[i] != -1:
            self.inOrder(self.right[i])

        if i == 0:
            return self.result

    def preOrder(self, i):
        if i == 0:
            self.result = []

        self.result.append(self.key[i])

        if self.left[i] != -1:
            self.preOrder(self.left[i])

        if self.right[i] != -1:
            self.preOrder(self.right[i])

        if i == 0:
            return self.result

    def postOrder(self, i):
        if i == 0:
            self.result = []

        if self.left[i] != -1:
            self.postOrder(self.left[i])

        if self.right[i] != -1:
            self.postOrder(self.right[i])

        self.result.append(self.key[i])

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(0)))
    print(" ".join(str(x) for x in tree.preOrder(0)))
    print(" ".join(str(x) for x in tree.postOrder(0)))


threading.Thread(target=main).start()
