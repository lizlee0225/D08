import random

def random_int():
	random_n = random.randint(0, 10)
	return random_n


def user_guess(n):
	print("Let's play the mimsmind0 game.")
	count = 0
	# Counts number of digits of the random integer.
	n_len = len(str(n))
	# User types in first guess.
	user_n = input("Guess a {}-digit number: ".format(n_len))
	while True:
		# Counts number of tries.
		count += 1
		# Checks if user input is an integer.
		try:
			user_n = int(user_n)
		except:
			user_n = input("Please enter an integer number: ")
			continue
		# Program provides basic feedback to the user.
		if user_n < n:
			user_n = input("Try again. Guess a higher number: ")
			continue
		elif user_n > n:
			user_n = input("Try again. Guess a lower number: ")
			continue
		else:
			print("Congratulations. You guessed the correct number in {} tries.".format(count))
			break


def main ():
	user_guess(random_int())

if __name__ == '__main__':
	main()