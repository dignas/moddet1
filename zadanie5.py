import pomocnicze_zadania_3_5 as p35

import matplotlib.pyplot as plt
import numpy as np
import math


def g(y, x):
	return y**2 - 1/x


def plot_abs_err(a, xs, err, n):
	a.plot(xs, err, 'g')
	a.set_xlabel('x')
	a.set_ylabel('absolute error')
	a.set_title(f'Absolute error for {n} iterations')


if __name__ == "__main__":
	h = 0.000001
	_, axs = plt.subplots(2, 2)
	axs = axs.reshape(-1)
	for n in range(4):
		n_iter = n + 1
		axis = axs[n]
		xs = []
		abserr = []
		for x in range(1, 1001):
			numerical_solution = p35.solve_n_iterations(
				lambda y, v=x: g(y, v),
				1,
				h,
				n_iter,
			)
			if math.isnan(numerical_solution):
				print(f"Error in numerical solution for n={n}, x={x}. Change x0.")
				break
			numerical_solution = np.abs(numerical_solution)
			math_solution = 1 / np.sqrt(x)
			xs.append(x)
			abserr.append(np.abs(numerical_solution - math_solution))
		plot_abs_err(axis, xs, abserr, n_iter)
	plt.show()
