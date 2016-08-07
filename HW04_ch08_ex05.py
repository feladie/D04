# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

'''Returns the word with each of its characters rotated n times.'''
def rotate_word(word, n):
	result = '' # Result string
	for letter in word:
		new_letter_num = ord(letter) + n
		if letter.islower():
			if new_letter_num < 97:	
				new_letter_num = 123 - (97 - new_letter_num) 
			result += chr(new_letter_num)		
		else:
			if new_letter_num < 64:
				new_letter_num = 91 - (65 - new_letter_num)
			result += chr(new_letter_num)
	return result		

def main():
	rotate_word('Python', 1)
	rotate_word('cheer', 7)
	rotate_word('melon', -10)
	rotate_word('MELON', -10)


if __name__ == '__main__':
    main()