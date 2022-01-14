# python3

import sys, threading
import math as m

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        if self.n != 0:
            self.key = [0 for i in range(self.n)]
            self.left = [0 for i in range(self.n)]
            self.right = [0 for i in range(self.n)]
            for i in range(self.n):
                [a, b, c] = map(int, sys.stdin.readline().split())
                self.key[i] = a
                self.left[i] = b
                self.right[i] = c

    def is_bst(self, root, lower_bound, upper_bound, validity):
        if not lower_bound < upper_bound:
            return False

        if validity and self.left[root] != -1:
            validity = self.is_bst(self.left[root], lower_bound, self.key[root], validity)

        if validity and self.right[root] != -1:
            validity = self.is_bst(self.right[root], self.key[root]-1, upper_bound, validity)

        if validity:
            return lower_bound < self.key[root] < upper_bound

        return validity


def main():
    tree = Tree()
    tree.read()
    if tree.n == 0:
        print("CORRECT")
        return
    if tree.is_bst(0, -m.inf, m.inf, True):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
