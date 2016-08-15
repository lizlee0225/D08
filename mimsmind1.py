import random

def random_int():
	random_n = random.randint(000, 1000)
	return random_n

def list_num(n):
	list_n = [value for value in str(n)]
	return list_n

def user_guess(n):
	n_len = len(str(n))
	maxrounds = (2**n_len) + n_len
	print("Let's play the mimsmind1 game. You have {} guesses.".format(maxrounds))
	count = 1
	# User types in first guess.
	user_n = input("Guess a {}-digit number: ".format(n_len))
	while count <= maxrounds:
		# Ends the game if user guesses maximum amount.
		if count == maxrounds:
			print("Sorry you did not guess the number in {} tries. The correct number is {}.".format(maxrounds, n))
			break
		cow = 0
		bull = 0
		count += 1
		# Checks if user input is an integer.
		try:
			user_n = int(user_n)
		except:
			user_n = input("Invalid input. Try again: ")
			continue
		if user_n == n:
			print("Congratulations. You guessed the correct number in {} times.".format(count))
			break
		# Translates user input and random number into a list in order to check individual digit. 
		user_list = list_num(user_n)
		random_list = list_num(n)
		for index, value in enumerate(random_list):
			if value not in user_list:
				continue
			# Checks if the same value is in the same location and replaces the value so it does not get checked again.
			elif index == user_list.index(value):
				bull += 1
				user_list[index] = 'B'
			# Checks if the value is in the list with remaining numbers.
			elif value in user_list:
				cow += 1
		user_n = (input("{} bull(s), {} cow(s). Try again: ".format(bull, cow)))


def main():
	user_guess(random_int())

if __name__ == '__main__':
	main()