''' Running the program will supply a written overview of the project
Bug: Sometimes, there are large gaps between results. Still unsure why '''


# ----------------------------- Imports ----------------------------------

import random
import os

# ------------------------------ Constants -----------------------------

# I have found that this only works well on some systems
# The program looks nicer with these colors, but they aren't necessary
#red = '\033[1;31;40m'
#white = '\033[1;37;40m'
#blue = '\033[1;34;40m'
#green = '\033[1;32;40m'
#yellow = '\033[1;33;40m'
#purple = '\033[1;35;40m'
red = ''
white = ''
blue = ''
green = ''
yellow = ''
purple = ''

# ------------------------------ Definitions ----------------------------

def make_deck():
	'''Makes a deck of cards
	Input: None
	Output: List of a shuffled deck of cards
	'''
	
	deck = []
	for number in range(2, 15):
		for suite in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
			if number == 11:
				deck.append(['Jack', suite])
			elif number == 12:
				deck.append(['Queen', suite])
			elif number == 13:
				deck.append(['King', suite])
			elif number == 14:
				deck.append(['Ace', suite])
			else:
				deck.append([number, suite])
	random.shuffle(deck)
	return deck

def run_game(deck):
	'''Plays handhold solitaire to completion
	Input: Deck to be used
	Output: None
	'''
	# Plays until the deck runs out
	while len(deck) > 0:
		flip.append(deck.pop(0))
		#print(flip)
		len_flip_before = 0
		# This loop ensures if multiple eliminations can happen from one flip
		while len_flip_before != len(flip):
			len_flip_before = len(flip)
			# Try is used in case flip is small enough that the elements are out of range
			try:
				if flip[-4][0] == flip[-1][0]:
					#print('Numbers match')
					for i in range(4):
						pile.append(flip.pop())
				if flip[-4][1] == flip[-1][1]:
					if flip[-1][1] == flip[-2][1] and flip[-1][1] == flip[-3][1]:
						#print('4 suites match')
						for i in range(4):
							pile.append(flip.pop())
					else:
						#print('2 suites match')
						pile.append(flip.pop())
						pile.append(flip.pop(-3))
			except:
				continue

def game_recycle(wins):
	'''Plays handheld solitaire until winning n times, 
	recycling the same cards to be used in the next game without shuffling
	Stats are given at the end
	Input: Number of desired wins 
	Output: None
	'''
	# Total calculates total number of games
	total = 0
	# Attempts keeps a list of how many games were played for each win
	attempts = []
	loading_increment = int(wins/100)
	loading = 0
	for i in range(wins):
		# Tries counts how many games are played before winning
		tries = 0
		skip = 1
		deck = make_deck()
		while True:
			# The first deck is random, but the other decks are recycled until a win occurs
			if skip != 1:
				deck = []
				flip.reverse()
				pile.reverse()
				deck.extend(flip)
				deck.extend(pile)
			skip = 0
			flip.clear()
			pile.clear()
			run_game(deck)
			tries += 1
			if len(flip) == 0:
				break
			# If tries reaches 100, 99.99% chance it reached a perpetual
			if tries == 100:
				break
		#print(tries)
		attempts.append(tries)
		total += tries
		if loading_increment != 0:
			if i % loading_increment == 0:
				loading += 1
				# clears screen
				print(chr(27)+'[2j' + '\033c' + '\x1bc')
				# Alternative loading bars
				#print(str(loading), end = ' ')
				print('|' + '|' * loading + ' ' * (100 - loading) + '|', end = '')

	# Count the perpetuals and then take them out of the list of attempts
	perpetuals = attempts.count(100)
	for i in range(perpetuals):
		attempts.remove(100)
		total -= 100	
	
	# Clears screen
	# print(chr(27)+'[2j' + '\033c' + '\x1bc')

	print('\n{}Total{} games: {}' .format(purple, white, total))
	print('{0}Average{1} number of games per win: {2:.2f}' .format(purple, white, total/(wins - perpetuals)))
	print('{}Maximum{} number of games played in a row without winning: {}' .format(purple, white, max(attempts)))
	print('{0}Percentage{1} likelihood to enter a perpetual: {2:.2f}%' .format(purple, white, (perpetuals/wins) * 100)) 
	print('(A perpetual is where the deck enters a cycle that can\'t be broken and also can\'t result in a win)')

def game_normal(wins):
	'''Plays handheld solitaire until the program wins n times
	Stats are given at the end
	Input: Number of wins
	Output: None
	'''
	# Total calculates number of games
	total = 0
	# Attempts keeps a list of how many games were played for each win
	attempts = []
	loading_increment = int(wins / 100)
	loading = 0
	for i in range(wins):
		# Tries counts how many games are played for each win
		tries = 0
		while True:
			# Deck is always random
			deck = make_deck()
			flip.clear()
			pile.clear()
			run_game(deck)
			tries += 1
			if len(flip) == 0:
				break
		#print(tries)
		attempts.append(tries)
		total += tries
		
		if loading_increment != 0:
			if i % loading_increment == 0:
				loading += 1
				# clears screen
				print(chr(27)+'[2j' + '\033c' + '\x1bc')
				# Alternative loading bar
				#print(str(loading), end = ' ')
				print('|' + '|' * loading + ' ' * (100 - loading) + '|')
		
	# Clears screen
	# print(chr(27)+'[2j' + '\033c' + '\x1bc')
		
	print('\n{}Total{} games: {}' .format(purple, white, total))
	print('{0}Average{1} number of games per win: {2:.2f}' .format(purple, white, total/wins))
	print('{}Maximum{} number of games played in a row without winning: {}' .format(purple, white, max(attempts)))
	
# ----------------------------------------- Main Code ----------------------------------------------------

# List of cards that have been flipped and not eliminated
flip = []
# List of cards that have been eliminated
pile = []

# Introduction
print('{}Welcome! This code is for gathering data on handheld solitaire.'.format(white))

print('\n{}Normal{} handheld solitaire is played by shuffling a deck of cards and pulling the cards out from the back one by one to form a new pile.' .format(red, white))
print('Any time the top card and the 4th card down have the same number, both cards and the two in between are taken away.')
print('Any time the top card and the 4th card down have the same suite, the two cards between them are taken away.')
print('Finally, any time the 4 top cards all have the same suite, all 4 are taken away.')
print('You win if you can take away every card from the new stack.')

print('\nPretty simple, huh?')

print('\nThe frustration you will run into rather quickly is that you will get through the entire deck without taking away every card.')
print('This leaves you with a mere small (or big) pile of cards and a heart full of sadness.')
print('So I wondered, how often do you actually win this game? It can\'t be often, or so my experiences told me.')

print('\nSo, this code will win the game for a set number of times and return the stats for how many games it takes to win on average.')
print('It will also return the longest game played so you can have a sense of the horrible misfortune you may experience in real life.')

print('\nAnd finally, it also includes another version of this game. I call it the {}recycling{} version.' .format(blue, white))
print('This version plays the game once, and if you lose, it uses the exact same deck without shuffling again.')
print('The question is, does this actually increase the frequency in which you win the game?')
print('Guess you\'ll have to find out yourself.')

#print('\nSIDE NOTE: The program looks like it runs a random string of numbers across the screen.')
#print('These are the number of games it took for the program to win.')
#print('If you choose for the program to run until it wins 1234 times, you will indeed see 1234 numbers run across the screen before the program completes.')

print('\nThat is all. Happy stat hunting!\n')

input('(You too!)')

print('\n---------------------------------------------\n')

while True:
	# Request game type
	print('What game would you like to play?')	
	print('Options: {0}Normal Handheld Solitaire{2} (N) or {1}Handheld Solitaire with Recycling{2} (R)\n' .format(red, blue, white))
	
	# Make sure game input is valid and request another input if not
	while True:
		game = input('Game: ').strip().upper()
		if not(game == 'N' or game == 'R'):
			print('\nTry another input\n')
			continue
		break
		
	# Request number of wins
	print('\nGreat! How many {}wins{} would you like the program to achieve?\n' .format(green, white))
	
	# Make sure wins input is valid and request another input if not
	while True:
		wins = input('Wins: ').strip()
		try:
			wins = int(wins)
		except:
			print('\nTry another input\n')
			continue
		# Confirms if user chooses very large number of wins
		if wins > 5000:
			print('\nWoah there! That\'s a big number! The program will take a very long time to run this.')
			print('Do you still want to continue?\n')
			while True:
				confirm = input('Y/N : '). strip().upper()
				if not (confirm == 'Y' or confirm == 'N'):
					print('\nTry another input\n')
					continue
				break
			if confirm == 'Y':
				break
			# Sends user back to choose number of wins if they do not confirm
			if confirm == 'N':
				print('\nI thought that seemed a little ambitious. Try another number.\n')
				continue
		break
	
	# Assign the name of the game based on what the user chose
	if game == 'N':
		game_name = red + 'Normal Handheld Solitaire' + white
	else:
		game_name = blue + 'Handheld Solitaire with Recycling' + white
		
	# Confirming the game type and number of wins
	print('\nGreat! Confirm: You want the program to win {} {}{}{} times.\n' .format(game_name, green, wins, white))

	# Makes sure the Y/N input is valid and requests another input if not'
	while True:
		response = input('Y/N : '). strip().upper()
		if not (response == 'Y' or response == 'N'):
			print('\nTry another input\n')
			continue
		break
		
	# If user does not confirm, user is sent back to start the whole process again
	if response == 'N':
		print('\nOh no! Let\'s put you back at the beginning.\n')
		input('(Okay!)')
		print()
		continue
	# If user confirms, program continues
	else:
		print('\nLet\'s get started!\n')
		input('(Okay!)')
		print()
		
	# Runs the program 
	if game == 'N':
		game_normal(wins)
		print()
	if game == 'R':
		game_recycle(wins)
		print()
	
	print('--------------------------------------------------------------------------------------')
		
	# Asks if they want to run another game
	print('\nRequest completed! Would you like to play another game?\n')
	
	# Checks to make sure inputs are valide and request another input if not
	while True:
		response = input('Y/N : '). strip().upper()
		if not (response == 'Y' or response == 'N'):
			print('\nTry another input\n')
			continue
		break
	
	# If user wants another game, they are sent back to the start
	if response == 'Y':
		print('\nSweet!', end = ' ')
		continue
	# If user does not want another game, code terminates
	else:
		print('\nOkay! Have a great day!')
	
	break
