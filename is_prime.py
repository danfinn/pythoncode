#!/usr/bin/python

number = int(raw_input("Enter a number and I'll check if it's a prime or not: "))

def check_prime(num):
	if num <= 1:
		return False
	else:
		for i in range(2, num):
			if num % i == 0:
				return False
		return True

if check_prime(number):
	print number, "is a prime number"
else:
	print number, "is not a prime number"

