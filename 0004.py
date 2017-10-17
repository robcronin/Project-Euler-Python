# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers

def largestPalindrome(n):
	start = 10 ** (n-1)
	end = (10 ** n) - 1
	ans = 0


	# loop down all is
	for i in range(end, start, -1):
		# only loop <= js to avoid testing same pair twicw
		for j in range(i, start, -1):
			# break from j if can't beat max so far
			if(i*j < ans):
				break
			# else check if palindrome and update answer if so
			elif str(i*j) == str(i*j)[::-1]:
					ans = i*j
		# break out of i loop if can't beat max so far
		if(i*i < ans):
				break

	return ans


print largestPalindrome(3)
