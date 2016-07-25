import random
from collections import defaultdict
import matplotlib.pyplot as plt

def get_arrivals(total_time):
	return [random.uniform(0, total_time), random.uniform(0, total_time)] # L and B

def run_once(l_wait, b_wait, total_time):
	l, b = get_arrivals(30)
	if 0 <= l - b <= b_wait or 0 <= b - l <= l_wait: return 1	
	return 0

def run_n(l_wait, b_wait, total_time, n):
	n_runs = [run_once(l_wait, b_wait, total_time) for _ in xrange(n)]
	return sum(n_runs)/float(len(n_runs))

def plot(l_wait, b_wait, total_time, n, k):
	plt.hist([run_n(l_wait, b_wait, total_time, n) for _ in xrange(k)], bins=20)
	plt.show() # CLT

if __name__ == '__main__':
	l_wait, b_wait, total_time = 5, 7, 30
	plot(l_wait, b_wait, total_time, 10000, 1000)