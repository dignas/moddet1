import numpy as np


def df(f, x, h):
	return (f(x + h) - f(x)) / h

def solve(f, x0, h):
	n = 0
	nmax = 1e6
	xn = x0
	epsilon = 1e-14
	while abs(f(xn)) > epsilon:
		if n >= nmax:
			return np.nan
		dfxn = df(f, xn, h)
		if dfxn == 0:
			return np.nan
		xn = xn - (f(xn) / dfxn)
		n += 1
	print(f"Result: {xn}")
	return n

def solve_n_iterations(f, x0, h, nmax):
	n = 0
	xn = x0
	epsilon = 1e-14
	while abs(f(xn)) > epsilon and n < nmax:
		dfxn = df(f, xn, h)
		if dfxn == 0:
			return np.nan
		xn = xn - (f(xn) / dfxn)
		n += 1
	return xn
