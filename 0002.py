# Project Euler Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

def brute(n):
	fib1, fib2 = 1, 1
	sumTotal = 0
	temp = 0

	# finds next fib and checks if even
	while(fib2 <= n):
		if(fib2 % 2 == 0):
			sumTotal += fib2
		temp = fib2
		fib2 += fib1
		fib1 = temp

	return sumTotal

def	onlyEven(n):
	fib1, fib2, fib3 = 1, 1, 2
	sumTotal = 0

	# since only every 3rd fib is even, calc 3 at a time
	while fib3 <= n:
		sumTotal += fib3
		fib1 = fib2 + fib3
		fib2 = fib1 + fib3
		fib3 = fib1 + fib2
	return sumTotal


#n = 4000000000000000000000000000000000**999
n = 4000000
#print brute(n)
print onlyEven(n)
