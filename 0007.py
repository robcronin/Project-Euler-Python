# Project Euler Problem 7
# What is the 10 001st prime number?

from primeMod import primeNumber


n = 10001

primes = primeNumber(10001)
print primes[len(primes)-1]

