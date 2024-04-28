# the episode 67:
import random
words = ["good", "bad", "ugly"]
random_word = random.choice(words)
# اعرض مسافات بنفس عدد حروف الكلمة 
display = []
for letter in random_word:
    display.append("_")
print(display)
lives = 6
while "_" in display and lives > 0:
   guessed = input("Please guess a letter: ").lower()
   if guessed not in random_word:
      lives -= 1
   for position in range (len(random_word)):
      if random_word[position] == guessed:
         display[position] = guessed
   print(display)
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
