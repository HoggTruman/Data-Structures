# python3
import sys


class Solver:
	def __init__(self, k, t, p):
		self.k, self.t, self.p, self.p_len = k, t, p, len(p)
		self.m, self.x = 1000000007, 263

		self.ht = [0]*(len(t)+1)
		self.hp = [0]*(len(p)+1)
		for i in range(1, len(t)+1): self.ht[i] = (self.x*self.ht[i-1] + ord(t[i-1])) % self.m
		for i in range(1, len(p)+1): self.hp[i] = (self.x*self.hp[i-1] + ord(p[i-1])) % self.m
		self.powers = [1]*(self.p_len+1)
		for i in range(1, self.p_len+1): self.powers[i] = (self.powers[i-1]*self.x) % self.m

	def ask(self, a_t, a_p, l):
		#a = l_t, l = pattern length,
		if (self.ht[a_t + l] - self.powers[l] * self.ht[a_t]) % self.m == (self.hp[a_p + l] - self.powers[l] * self.hp[a_p]) % self.m:
			return True
		return False

	def match(self, l_t, r_t, l_p, r_p, mismatches):
		if l_t <= r_t:
			if self.ask(l_t, l_p, r_t-l_t+1):
				return mismatches

			piv_t = (l_t + r_t)//2
			piv_p = (l_p + r_p)//2

			if not self.ask(piv_t, piv_p, 1):
				mismatches += 1
			if mismatches > self.k:
				return mismatches
			mismatches = self.match(l_t, piv_t-1, l_p, piv_p-1, mismatches)
			if mismatches > self.k:
				return mismatches
			mismatches = self.match(piv_t+1, r_t, piv_p+1, r_p, mismatches)
		return mismatches

	def execute(self):
		result = []
		for i in range(len(t) - self.p_len + 1):
			if self.match(i, i + self.p_len - 1, 0, self.p_len - 1, 0) <= self.k:
				result.append(i)
		return result




for line in sys.stdin.readlines():
	k, t, p = line.split()
	solver = Solver(int(k), t, p)
	ans = solver.execute()
	print(len(ans), *ans)
