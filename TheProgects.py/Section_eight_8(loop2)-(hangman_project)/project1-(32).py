# the episode 64
import random 
words = ["office", "panda", "cabin", "ginger"]
random_word = random.choice(words)
guess = input("Please guess a letter: ").lower()
for letter in random_word:
    if guess in letter:
        print("Right")
    else:
        print("Wrong")