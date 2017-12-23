#!/usr/bin/env python
import sys
import time

def getLargestPrimeFactor(a):
	b = 2
	while (a > b):
		if (a % b == 0):
			a = a / b
			b = 2
		else:
			b += 1;
	return b

if __name__ == '__main__':
	start_time = time.time()
	print(getLargestPrimeFactor(int(sys.argv[1])))
	print("--- %s seconds ---" % (time.time() - start_time))
