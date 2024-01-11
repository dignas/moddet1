import math

def init_segment(A, B, n):
	return [A + (k / n) * (B - A) for k in range(0, n + 1)]

def get_f_values_for_segment(f, seg):
	return [(x, f(x)) for x in seg]

def plot_func(f_values, label, axes):
	x, y = zip(*f_values)
	axes.plot(x, y, label=label)

def plot_funcs(axes, xlabel, ylabel, title, **f_values_list):
	for label, f in f_values_list.items():
		plot_func(f, label, axes)
	axes.set_xlabel(xlabel)
	axes.set_ylabel(ylabel)
	axes.set_title(title)
	axes.legend()

def get_h(A, B, n):
	return (B - A) / n

def get_n(A, B, h):
	return math.floor((B - A) / h)
