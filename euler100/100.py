p = 3
q = 2
k = -2
r = 4
s = 3
l = -3
 
b = 15
n = 21
while n < 10 ** 12:
	b, n = (p * b + q * n + k, r * b + s * n + l)
print("The result is:", b)
