# Project Euler Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000


def brute(n):
	sumTotal = 0

	# loop through and all multiples of 3 and 5
	for i in range(1, n):
		if i % 3 == 0:
			sumTotal += i
		elif i % 5 == 0:
			sumTotal += i
	
	return sumTotal


def chooseMultiples(n):
	sumTotal = 0

	# add all 3s
	for i in range(3, n, 3):
		sumTotal += i

	# set i to 0 in case n < 15
	i = 0	

	# add all 5, 10 mod 15s
	for i in range(15, n, 15):
		sumTotal += 2*i - 15

	# add extras leftover at end
	for i in range(i+5, n, 5):
		sumTotal += i
	
	return sumTotal


n = 1000
#print "Brute is " + str(brute(n))
print "Mult is " + str(chooseMultiples(n))
