#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def guess_the_number():

	count = 1 # counter to track how many times the user has guessed
	answer = random.randint(1, 25) # creates a random integer from 1 - 25

	while (count <= 5):	
		count += 1 
		try: 
			guess = int(input('Guess a number from 1 to 25: ')) # asks the user to guess what the number is 
		except: 
			print('Please guess an INTEGER.')	# if the user doesn't enter an int, throw an exception
			continue 
		if guess == answer: # user answers correct answer
			print('Nice! The answer is ', answer)
			break
		elif guess > answer:	# guess is too high
			if guess > 26:
				print('Guess a number between 1 to 25')
			else:
				print('Too high')
		else:	# guess is too low	
			if guess < 1:
				print('Guess a number between 1 to 25')
			else:
				print('Too low')	
	else:						# five guesses have been made without the right answer
		print('Game over')			

################################################################################
def main():

	guess_the_number()
    
    

if __name__ == '__main__':
    main()