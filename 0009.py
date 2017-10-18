# Project Euler Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

n = 1000

for a in range(1, n/2 + 1):
	for b in range(a, n/2 + 1):
		c = n - a - b
		if(a*a + b*b == c*c):
			print a*b*c
