# python3

import sys


def PolyHash(S,p,x):
	ans = 0
	for c in reversed(S):
		ans = (ans*x+ord(c)) % p
	return ans


class Solver:
	def __init__(self, s):
		self.s = s
		n = len(s)
		self.m1, self.m2, self.x = 10**9 + 7, 10**9 + 9, 7
		self.h1 = [0]*(n+1)
		self.h2 = list(self.h1)
		for i in range(1, n+1):
			self.h1[i] = (self.x*self.h1[i-1] + ord(s[i-1])) % self.m1
			self.h2[i] = (self.x*self.h2[i-1] + ord(s[i-1])) % self.m2


	def ask(self, a, b, l):
		if (self.h1[a+l] - pow(self.x,l,self.m1)*self.h1[a]) % self.m1 == (self.h1[b+l] - pow(self.x,l,self.m1)*self.h1[b]) % self.m1:
			if(self.h2[a+l] - pow(self.x,l,self.m2)*self.h2[a]) % self.m2 == (self.h2[b+l] - pow(self.x,l,self.m2)*self.h2[b]) % self.m2:
				return True
		return False


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
