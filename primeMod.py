import math

# Sieve of Eratosthenes for max prime
def sieve(end):
	checklist = ["n", "n"] + ["y"]*(end-1)
	primes = []
	root = int(math.sqrt(end)) + 1
	for i in range(2, root):
		if checklist[i] == "y":
			primes.append(i)
			for j in range(i*i, end+1, i):
				checklist[j] = "n"
	for i in range(root, end+1):
		if checklist[i] == "y":
			primes.append(i)
		


	return primes

# Basic prime finder for number of primes
def primeNumber(end):
	primes = [2, 3]
	size = len(primes)

	index = 5
	while(size < end):
		root = int(math.sqrt(index)) + 1
#print "For " + str(index) ", root is " + str(root)

		add = True
		for i in primes:
			if(i > root):
				break
			elif index % i == :
				add = False
				break
		if(add):
			primes.append(index)
			size += 1

		index +=2
		


	return primes

# Factors of Primes
def primeFactors(n, primes):
	count = [0]*len(primes)

	for i in range(0, len(primes)):
		prime = primes[i]
		while n%prime == 0:
			n /= prime
			count[i] += 1

		if n == 1:
			return count
	print "ERROR"
	return count
