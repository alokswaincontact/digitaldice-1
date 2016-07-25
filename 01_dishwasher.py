import random
from collections import defaultdict
import matplotlib.pyplot as plt

def get_rand():
	counter = defaultdict(int)
	for _ in range(5): counter[random.randint(1,5)] += 1
	return counter

def run_once():
	clumsy = random.randint(1,5)
	for val, freq in get_rand().items():
		if freq >= 4 and val == clumsy: return 1
	return 0

def run_n(n):
	n_runs = [run_once() for _ in xrange(n)]
	return sum(n_runs)/float(len(n_runs))

def plot(n, k):
	plt.hist([run_n(n) for _ in xrange(k)], bins=20)
	plt.show() # CLT

if __name__ == '__main__':
	plot(1000, 2000)