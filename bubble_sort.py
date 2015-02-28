#!/usr/bin/python

list = [8,7,12,4,9,6,5]

def bubbleSort(list):
	for passNum in range(len(list)-1,0,-1):
		for num in range(passNum):
			current = list[num]
			forward = list[num +1]
			if current > forward:
				list[num] = forward
				list[num +1]=current

bubbleSort(list)
print list
