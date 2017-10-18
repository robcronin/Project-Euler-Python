# Project Euler Problem 3
# What is the largest prime factor of the number 600851475143

def largestPrimeFactor(n):
	ans = 2

	while(n % ans == 0):
			n = n/ans

	if(n == 1):
			return 2
	else:
		ans = 3

	while(n != 1):
		if n % ans == 0:
			n = n/ans
		else:
			ans = ans + 2

	return ans

n = 600851475143
print largestPrimeFactor(n)
