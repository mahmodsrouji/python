# the episode 66:
import random
words = ["good", "bad", "ugly"]
random_word = random.choice(words)
# اعرض مسافات بنفس عدد حروف الكلمة 
display = []
for letter in random_word:
    display.append("_")
print(display)
while "_" in display:
   guessed = input("Please guess a letter: ").lower()
   for position in range (len(random_word)):
      if random_word[position] == guessed:
         display[position] = guessed
   print(display)
print("""
         ********
         YOU WIN!
         ********
""")