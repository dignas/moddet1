import funkcje_zadania_1_2 as f12
import pomocnicze_zadania_1_2 as p12

import numpy as np
import matplotlib.pyplot as plt

def numerical_integral_left(f, n):
	seg = p12.init_segment(f12.A, f12.B, n)
	h = p12.get_h(f12.A, f12.B, n)
	vals = p12.get_f_values_for_segment(f, seg)
	return h * np.sum(vals[:-1], axis=0)[1]

def numerical_integral_right(f, n):
	seg = p12.init_segment(f12.A, f12.B, n)
	h = p12.get_h(f12.A, f12.B, n)
	vals = p12.get_f_values_for_segment(f, seg)
	return h * np.sum(vals[1:], axis=0)[1]

def numerical_integral_trapez(f, n):
	seg = p12.init_segment(f12.A, f12.B, n)
	h = p12.get_h(f12.A, f12.B, n)
	vals = p12.get_f_values_for_segment(f, seg)
	return h * (np.sum(vals[1:-1], axis=0)[1] + 0.5*vals[0][1] + 0.5*vals[len(vals)-1][1])

def error_function(numerical_integral, math_integral):
	return abs(numerical_integral - math_integral)

def check_function(f, integral, axes, function_title):
	h_step = 0.0001
	h_start = 0.0001
	h_number = 10000
	error_function_left_values = []
	error_function_right_values = []
	error_function_trapez_values = []
	prev_n = None

	for i in range(0, h_number):
		h_work = h_start + i * h_step
		n = p12.get_n(f12.A, f12.B, h_work)

		if prev_n is not None and prev_n == n:
			continue
		prev_n = n

		h = p12.get_h(f12.A, f12.B, n)
		i_left = numerical_integral_left(f, n)
		i_right = numerical_integral_right(f, n)
		i_trapez = numerical_integral_trapez(f, n)

		error_function_left_values.append((h, error_function(i_left, integral)))
		error_function_right_values.append((h, error_function(i_right, integral)))
		error_function_trapez_values.append((h, error_function(i_trapez, integral)))
	
	p12.plot_funcs(axes=axes, ylabel="Absolute error", xlabel="h", title=f"Error functions for {function_title} numerical integrals",
		left_point=error_function_left_values, right_point=error_function_right_values, trapezium=error_function_trapez_values)


if __name__ == "__main__":
	_, axs = plt.subplots(3, 1)
	check_function(f12.f1, f12.if1, axs[0], "cos(x)")
	check_function(f12.f2, f12.if2, axs[1], "cos(100x)")
	check_function(f12.f3, f12.if3, axs[2], "sin(x)/x")

	plt.show()
