import random
hangmanpics = [''' 
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["good", "bad", "ugly"]
random_word = random.choice(words)
# اعرض مسافات بنفس عدد حروف الكلمة 
display = ["_"] * len(random_word)
print(' '.join(display))
print(hangmanpics[0])
lives = 6
invalid_words = []
while "_" in display and lives > 0:
   guessed = input("Please guess a letter: ").lower()
   if guessed in invalid_words:
      print("You have already type this answer! ")
      print(f" You have {lives} more tries")
      continue
   invalid_words.append(guessed)
   if guessed not in random_word:
      lives -= 1
      print(hangmanpics[7-lives])
   else:
      for position in range (len(random_word)):
         if random_word[position] == guessed:
            display[position] = guessed
   print(' '.join(display))
   print(f" You have {lives} more tries")
if lives == 0:
   print("""
         You Lose!
   """)
else:
   print("""
         ********
         YOU WIN!
         ********
   """)

        