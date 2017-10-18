# Project Euler Problem 10
# Find the sum of all the primes below two million

import math

# Sieve of Eratosthenes for max prime
def sieveSum(end):
	checklist = ["n", "n"] + ["y"]*(end-1)
	sumPrimes = 0
	root = int(math.sqrt(end)) + 1
	for i in range(2, root):
		if checklist[i] == "y":
			sumPrimes += i
			for j in range(i*i, end+1, i):
				checklist[j] = "n"
	for i in range(root, end+1):
		if checklist[i] == "y":
			sumPrimes += i
		


	return sumPrimes

print sieveSum(2000000)
