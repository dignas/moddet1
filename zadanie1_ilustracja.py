import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
	h = 0.01
	C = 1.1173
	xs = [-0.85 + h * i for i in range(91)]
	coss = [math.cos(x) for x in xs]
	tangent = [-math.sin(-0.5) * x + C if x < -0.2 else np.nan for x in xs]
	plt.plot(xs, coss)
	plt.plot(xs, tangent, 'r')
	plt.plot([-0.5], [math.cos(-0.5)], 'bo', label='asd')
	plt.vlines([-0.5 - 0.2, -0.5 + 0.2], 0.6, 1.1, linestyles='dashed')
	ax = plt.subplot(1, 1, 1)
	ax.set_xticks([-0.8 + i * 0.1 for i in range(9)])
	plt.show()
