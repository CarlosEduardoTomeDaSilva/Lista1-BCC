import math

a = float(input())
b = float(input())
c = float(input())

def volume():
	return a*b*c

def diagonal():
	sum = a**2 + b**2 + c**2
	return math.sqrt(sum)

print("Volume: {:.2f}".format(volume()), "Diagonal: {:.2f}".format(diagonal()))