import math
import scipy

def f1(x):
	return math.cos(x)

def f2(x):
	return math.cos(100 * x)

def f3(x):
	if x == 0:
		return 1
	return math.sin(x) / x

def df1(x):
	return -math.sin(x)

def df2(x):
	return -100 * math.sin(100 * x)

def df3(x):
	if x == 0:
		return 0
	return (x * math.cos(x) - math.sin(x)) / (x * x)


if1 = 2 * math.sin(1)
if2 = math.sin(100) / 50
__if3, _ = scipy.special.sici(1)
if3 = 2 * __if3

A = -1
B = 1
