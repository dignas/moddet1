import funkcje_zadania_1_2 as f12
import pomocnicze_zadania_1_2 as p12

import matplotlib.pyplot as plt
import numpy as np

def numerical_derivative_forward(f, n):
	seg = p12.init_segment(f12.A, f12.B, n)
	h = p12.get_h(f12.A, f12.B, n)
	return [(t, (f(t + h) - f(t)) / h) for t in seg[:-1]]

def numerical_derivative_backward(f, n):
	seg = p12.init_segment(f12.A, f12.B, n)
	h = p12.get_h(f12.A, f12.B, n)
	return [(t, (f(t) - f(t - h)) / h) for t in seg[1:]]

def numerical_derivative_central(f, n):
	seg = p12.init_segment(f12.A, f12.B, n)
	h = p12.get_h(f12.A, f12.B, n)
	return [(t, (f(t + h) - f(t - h)) / (2 * h)) for t in seg[1:-1]]

def error_function(numerical_derivative, df):
	abs_err = [abs(y - df(x)) for x, y in numerical_derivative]
	return np.mean(abs_err)

def check_function(f, df):
	h_step = 0.0001
	h_start = 0.0001
	h_number = 1000
	_, axs = plt.subplots(2, 2)
	axs = axs.reshape(-1)
	plot_at = [0, h_number // 2, h_number - 1]
	error_function_forward_values = []
	error_function_backward_values = []
	error_function_central_values = []

	for i in range(0, h_number):
		h = h_start + i * h_step
		n = p12.get_n(f12.A, f12.B, h)
		seg = p12.init_segment(f12.A, f12.B, n)

		d_forward = numerical_derivative_forward(f, n)
		d_backward = numerical_derivative_backward(f, n)
		d_central = numerical_derivative_central(f, n)
		d_math = p12.get_f_values_for_segment(df, seg)

		try:
			ax_index = plot_at.index(i)
			p12.plot_funcs(axes=axs[ax_index], ylabel="Derivative", xlabel="x", title=f"Numerical and math derivative for h={h:.4f}",
				forward=d_forward, backward=d_backward, central=d_central, math=d_math)
		except ValueError:
			pass

		error_function_forward_values.append((h, error_function(d_forward, df)))
		error_function_backward_values.append((h, error_function(d_backward, df)))
		error_function_central_values.append((h, error_function(d_central, df)))
	
	p12.plot_funcs(axes=axs[3], ylabel="Mean abs error", xlabel="h", title="Error functions",
		forward=error_function_forward_values, backward=error_function_backward_values, central=error_function_central_values)
	plt.show()

if __name__ == "__main__":
	check_function(f12.f1, f12.df1)
	check_function(f12.f2, f12.df2)
	check_function(f12.f3, f12.df3)
