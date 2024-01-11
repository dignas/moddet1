import pomocnicze_zadania_3_5 as p35

import math
import matplotlib.pyplot as plt


def g(x):
	return math.cos(x) - x


def plot_n_steps(a, hs, ns, x0):
	a.plot(hs, ns, 'ro', label='number of steps')
	a.set_xlabel('h')
	a.set_title(f'Convergence rate for x0={x0}')
	a.legend()


if __name__ == '__main__':
	start_points = [0, 1, 2, 5]
	_, axs = plt.subplots(2, 2)
	axs = axs.reshape(-1)

	for i in range(4):
		h_step = 0.01
		h_start = 0.01
		h_number = 100
		axis = axs[i]
		start_point = start_points[i]
		hs = []
		n_of_steps = []

		for i in range(0, h_number):
			h = h_start + i * h_step
			hs.append(h)
			n_of_steps.append(p35.solve(g, start_point, h))
		
		plot_n_steps(axis, hs, n_of_steps, start_point)

	plt.show()
