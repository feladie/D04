#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import math

# Body
def eval_loop():
	user_input = str(input('Input: '))
	done = 'done'
	last_exp = ''
	while (user_input != done):
		last_exp = repr(eval(user_input))
		print(last_exp)	
		user_input = str(input('Input: '))
	else: 
		return last_exp
	# Tried type(math.pi) as input, but it doesn't work. :(		

###############################################################################
def main():
    eval_loop()

if __name__ == '__main__':
    main()
