# Project Euler Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def sqDiff(n):
	sumTotal = 1
	sumOfSqs = 1

	for i in range(2, n+1):
			sumTotal += i
			sumOfSqs += i*i

	return sumTotal**2 - sumOfSqs


print sqDiff(100)
