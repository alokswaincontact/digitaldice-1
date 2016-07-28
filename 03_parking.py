import random
from collections import defaultdict
import matplotlib.pyplot as plt

figure = plt.figure()

def get_points(n, l=1):
	return [random.uniform(0, l) for k in range(n)]

def run_once(n):
	mutual_nn, nn_dict = 0, {}
	p = sorted(get_points(n))
	nn_dict[0], nn_dict[n-1] = 1, n-2
	for idx, val in enumerate(p[1:-1], 1):
		nn_dict[idx] = idx-1 if abs(val-p[idx-1]) < abs(val-p[idx+1]) else idx+1
	for n1, n2 in nn_dict.items():
		if nn_dict[n2] == n1: mutual_nn += 1 
	# divide by 2 for mutual pairs
	return mutual_nn

def run_n(num_points, n):
	n_runs = [run_once(num_points) for _ in xrange(n)]
	return sum(n_runs)/float(len(n_runs))

def plot_clt(num_points, n, k):
	ax1 = figure.add_subplot(121)
	ax1.hist([run_n(num_points, n)/float(num_points) for _ in xrange(k)], bins=20)
	# ax1.show() # CLT of R.V. proportion of mutual neighbors 

def plot_nn_wrt_n(min_points, max_points, n, step_points=1):
	x = range(min_points, max_points, step_points)
	y = [run_n(p, n) for p in x]
	ax2 = figure.add_subplot(122)
	ax2.plot(x, y)
	# ax2.show() # linear plot of number of mutual neighbors and total points

if __name__ == '__main__':
	print (run_n(10, 10000))/10.0
	plot_clt(50, 100, 1000)
	plot_nn_wrt_n(3, 30, 200)
	plt.show()