# Author: LeeTuah
# Word: now
# Team: Dillusioners

import os
import random
import time

class MemoryGame:
	# initializes the word
	def __init__(self):
		self.guess = ""
		for i in range(8):
			self.guess = self.guess + str(random.randint(0, 9))

	# main method
	def main(self):
		print("\t\t\tMemory Game\n")
		print("A number will be shown to you for two seconds.\nYou have to memorise it and type it in within 5 seconds.")
		name = input("Enter your name before we continue: ")
		print("Your number is: \n"+self.guess)
		time.sleep(2)
		os.system('clear')
		num = input("Enter the number now!(If you need screenshots what are you doing in life): ")
		if num == self.guess:
			print("The number you guessed now is right!")
		else:
			print("The number you guessed now is wrong!")

# object declaration and method call
game = MemoryGame()
game.main()
