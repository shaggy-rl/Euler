import math
def sumofdigits(x):
	answer = 0
	while ( x > 0):
		answer += x % 10
		x /= 10
	return answer

x = sumofdigits(math.factorial(100))
print x
