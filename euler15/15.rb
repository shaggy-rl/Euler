# Helping friend solve this problem in ruby

# Function Definition

def factorial(n)
	return 1 if n.zero?
	1.upto(n).inject(:*)
end

# Variables

num_right_down = 40
num_right = 20

# Solution

puts factorial(num_right_down) / (factorial(num_right) * factorial(num_right_down - num_right))
