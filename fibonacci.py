#!/usr/bin/python


def fibonacci(num):
	total = [0, 1]
	if num <= 1:
		print total
	else:
		for i in range(2, num):
			total.append(total[i-2] + total[i-1])
		print str(total)[1:-1]


fibonacci(19)
