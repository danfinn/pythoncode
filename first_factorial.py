#!/usr/bin/python
#
# A function to return the factorial of a given integer
# without using the built in math factorial function
#

#import cProfile

fact_input = int(raw_input("Enter an integer: "))

def first_factorial(num):
    if num == 0:
        return 0
    else:
        result = 1
        for i in range(1,num + 1):
            result *= i
        return result

print first_factorial(fact_input)

#cProfile.run('first_factorial(126000)')
