# Project Euler Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import primeMod

def minDivisible(n):
	primes = primeMod.sieve(n)
	primeCount = [1]*len(primes)

	ans = 1

	# multiply each of the primes
	for i in primes:
		ans *= i

	primeProd = ans	


	for j in range(4, n+1):
		if j not in primes:
			# for each non-prime get the number of each prime in factorisation
			count = primeMod.primeFactors(j, primes)
			for k in range(0, len(primes)):
				# if any count is larger than current count then multiply answer and update
				if count[k] > primeCount[k]:
					ans *= primes[k]**(count[k]-primeCount[k])
					primeCount[k] = count[k]

	return ans



print minDivisible(20)
