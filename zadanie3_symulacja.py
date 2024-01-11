from zadanie3 import g
from pomocnicze_zadania_3_5 import df

import matplotlib.pyplot as plt


if __name__ == "__main__":
	h = 0.05
	n = 0
	xn = 5
	epsilon = 1e-14
	ns = []
	xns = []
	dfxns = []
	while abs(g(xn)) > epsilon:
		ns.append(n)
		xns.append(xn)
		dfxn = df(g, xn, h)
		dfxns.append(dfxn)
		xn = xn - (g(xn) / df(g, xn, h))
		n += 1

	_, axs = plt.subplots(2, 1)
	axs[0].set_xticks(ns)
	axs[1].set_xticks(ns)
	axs[0].plot(ns, xns)
	axs[1].plot(ns, dfxns)
	plt.show()
