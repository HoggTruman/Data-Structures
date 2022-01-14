# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


class RollingSolver:
	def __init__(self, s, t):
		self.s = s
		self.t = t
		self.s_len = len(s)
		self.t_len = len(t)

	def hash_func(self, s, p, x):
		ans = 0
		for c in reversed(s):
			ans = (ans * x + ord(c)) % p
		return ans

	def pre_compute_hashes(self, T, P_len, p, x):
		T_len = len(T)
		Hashes = [0] * (T_len - P_len + 1)
		start = T[T_len - P_len:]
		Hashes[-1] = self.hash_func(start, p, x)
		y = 1
		for i in range(1, P_len + 1):
			y = (y * x) % p
		for i in range(T_len - P_len - 1, -1, -1):
			Hashes[i] = (x * Hashes[i + 1] + ord(T[i]) - y * ord(T[i + P_len])) % p
		return Hashes

	def bs_hash(self):
		l = 0
		r = min(self.s_len, self.t_len)
		k = (l + r) // 2 + 1
		best_i = True

		while l < r:
			k = (l + r) // 2 + 1
			s_hashlist = self.pre_compute_hashes(self.s, k, 1000000007, 263)
			t_hashlist = self.pre_compute_hashes(self.t, k, 1000000007, 263)
			s_hashes = {s_hashlist[i]: i for i in range(len(s_hashlist))}
			t_hashes = {t_hashlist[i]: i for i in range(len(t_hashlist))}
			found = False
			for key in s_hashes:
				if key in t_hashes:
					if self.hash_func(self.s[s_hashes[key]:s_hashes[key]+k], 1000000009, 111) == self.hash_func(self.t[t_hashes[key]:t_hashes[key]+k], 1000000009, 111):
						found = True
						l = k
						best_i = s_hashes[key]
						best_j = t_hashes[key]
						break
			if not found:
				r = k-1

		if k == 1 and best_i:
			return Answer(0, 0, 0)
		else:
			return Answer(best_i, best_j, l)



for line in sys.stdin.readlines():
	s, t = line.split()
	solver = RollingSolver(s, t)
	ans = solver.bs_hash()
	print(ans.i, ans.j, ans.len)
