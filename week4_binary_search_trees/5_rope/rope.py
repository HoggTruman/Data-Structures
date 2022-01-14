# python3

import sys


class Rope:
	def __init__(self, s):
		self.s = s

	def result(self):
		return self.s

	def process(self, i, j, k):
		ij_str = self.s[i:j+1]
		rem_str = self.s[:i] + self.s[j+1:]
		self.s = rem_str[:k] + ij_str + rem_str[k:]



rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
