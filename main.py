import random
from words import words

word = random.choice(words)
reveal = ["_"] * len(word)
lives = 6
gameWon = False
wrong_letters = []
# print(word.upper())
print("Hangman")


def hangman():
				while lives == 6:
								image = (" +-----+\n       |\n       |\n       |\n       |\n       |\n    -------")
								return image
				while lives == 5:
								image = (" +-----+\n O     |\n       |\n       |\n       |\n       |\n    -------")
								return image
				while lives == 4:
								image = (" +-----+\n O     |\n |     |\n       |\n       |\n       |\n    -------")
								return image
				while lives == 3:
								image = (" +-----+\n O     |\n/|     |\n       |\n       |\n       |\n    -------")
								return image
				while lives == 2:
								image = (" +-----+\n O     |\n/|\    |\n       |\n       |\n       |\n    -------")
								return image
				while lives == 1:
								image = (" +-----+\n O     |\n/|\    |\n/      |\n       |\n       |\n   -------")
								return image
				if lives == 0:
								image = (" +-----+\n O     |\n/|\    |\n/ \    |\n       |\n       |\n   -------")
								return image


while gameWon == False and lives > 0:
				print(reveal)
				print(hangman())
				print("Letters not in word:", wrong_letters)
				guess = input(f"guess a letter or a word you have {lives} lives remaining: ")

				if guess == word:
								gameWon = True
				if len(guess) == 1 and guess in word:
								for i in range(0, len(word)):
												letter = word[i]
												if guess == letter:
																reveal[i] = guess.upper()
								if '_' not in reveal:
												gameWon = True

				else:
								wrong_letters.append(guess.upper())
								lives -= 1

if gameWon == True:
				print("You Win!")
else:
				print(hangman())
				print("You lost the word was:", word.upper())
