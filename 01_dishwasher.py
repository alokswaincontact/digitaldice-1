import random
from collections import defaultdict
import matplotlib.pyplot as plt

def get_rand():
	counter = defaultdict(int)
	for _ in range(5): counter[random.randint(1,5)] += 1
	return counter

def aggregate(n):
	count, clumsy = 0, random.randint(1,5)
	for i in range(n):
		rand = get_rand()
		for val, freq in rand.items():
			if freq >= 4 and val == clumsy: count += 1
	return count/float(n)

def simulate(n, k):
	return [aggregate(n) for _ in range(k)]

def plot(simulations):
	plt.hist(simulations, bins=10)
	plt.show()

if __name__ == '__main__':
	simulations = simulate(500, 5000)
	estimate = sum(simulations)/float(len(simulations))
	print ("estimate = %s" % estimate)
	plot(simulations)