#! /usr/bin/python
# Uses the russian peasant algorithim to add 2 numbers

num1 = int(raw_input('First number please: '))
num2 = int(raw_input('Second number please: '))

def russian_peasant(a,b):
  x = a; y =b
  z = 0

  while x > 0:
    if x % 2 == 1: z += y
    x = x >> 1
    y = y << 1

  return z

print russian_peasant(num1,num2)
