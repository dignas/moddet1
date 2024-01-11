import pomocnicze_zadania_3_5 as p35

import math


def g(x):
	return x**3 - x**2 - 1


if __name__ == "__main__":
	x0 = 2
	h = 0.001
	n = p35.solve(g, x0, h)

	if math.isnan(n):
		print(f"The method didn't converge.")
	else:
		print(f"Method converged after {n} steps.")
