import random 
print("""Welcome to the coin Gusseing Game!
Choose a method to toos the coin: 
1. Using random.random()
2. Using random.ranint()
""")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    if random.random() >= 0.5:
       com_result = "heads"
    else:
       com_result = "tails"
elif choice == 2:
    if random.randint(0, 1) == 0:
        com_result = "heads"
    else:
        com_result = "tails"
else:
    print("Invaild choice! Please chose (1) or (2)")

user_guess = (input("Enter your Guess (Heads or Tails): ")).lower()
if user_guess.lower() == com_result.lower():
    print("congratulations! You won")
    print(f"The computer coin toss result was: {com_result}")
elif user_guess != "tails".lower() and user_guess != "heads".lower():
    print("Invaild answer! Please type ('Heads' or 'Tails')")
else:
    print("Sorry, you lost!")
    print(f"The computer coin toss result was: {com_result}")
#This project has been modified and reviewed.

favorite_friends = ["Moafak", "Omar", "Mohamad", "Abdullah", "yazan"]
print(f"The first friend on our list is {favorite_friends[0]} and the last friend on our list is {favorite_friends[-1]}")
favorite_friends[1] = "Abu Mohamad"

#This project has been reviewed from Episode 35
color = []
do = input("Add the first color you like: ")
color.append(do)
q_color = input("Do you want to add more colors? Yes, or No? ").lower()
if q_color == "yes":
    do = input("Add another color to the list: ")
    color.append(do)
    print("The colors you like are")
    print(color)
elif q_color =="no".lower():
    print("The color you like is")
    print(color)
else:
    print("Invaild answer! please stick with 'Yes' or 'No ")


class_a = ["Tom","Silia", "Samer", "farah"]
class_b = ["Andrew", "Hadi", "Tina", "Samar", "Jacks"]
class_ab = class_a + class_b
class_ab.remove("Tina")


guess = input("Guess the name of the list below here: ")
if guess in class_ab:
    print("Good guess")
else:
    print("Sorry, better luck next time")

#This project has been reviewed from episode 42
#🐇🌿
#Welocme to place the rabbit
#Where should the rabbit go?
#Please choose a row and a colmun
#Success .....
print("Welcome to place the rabbit")
print("\nWhere should the rabbit go?🐇\n")
field = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}\n")
position = input("Please choose a row and a colmun ")
row = int(position[0])
colmun = int(position[1])
field[row-1][colmun-1] = "🐇"
print("\nSuccess .....\n")
print(f"{field[0]}\n{field[1]}\n{field[2]}")


# review on everything, 15/4/2024

length = float(input("Please type length: "))
width = float(input("Please type width: "))
price = float(input("How much for 1 meter: "))
area = length * width 
result = area * price
print(f"The total area is {area}")
print(f"Give the guy: {result}")
# another project
seconds = int(input("Please type the number of seconds: \n"))
hours = seconds // 3600
minutes = seconds % 3600 // 60
remaining_seconds = seconds % 60
print(f"This course is: {hours} hourse and {minutes} minutes and {remaining_seconds} seconds long")
# another project
mark = float(input("Type the mark here to rate: \n"))
if mark > 100:
    print("This number is not supported")
elif mark == 100:
    print("This mark is an excellent grade!")
elif mark >= 90:
    print("This mark is an excellent grade!")
elif mark >= 70:
    print("This mark is in a good grade!")
elif mark >= 50:
    print("This mark is in an acceptable grade!")
else:
    print("you got an f grad!")
# another project
words = ["yes", "no", "maybe"]
user_input = input("Enter one of the required words: \n").lower()
if user_input in words:
    print("you are answerd correctly")
else:
    print("your answer is incorrect")
# another project
# a slight modification
import random
print("Welcome to the coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")
chosen_number = int(input("Enter your choice(1 or 2): "))
if chosen_number == 1:
    if random.random() >= 0.5:
       computer_result = "heads"
    else:
       computer_result = "tails"     
elif chosen_number == 2:
  
     if random.randint(0,1) == 0:
       computer_result = "heads"
     else:
       computer_result ="tails"   
else:
   print("Invaild choice! please select either 1 or 2")      

user_guess = input("Enter your guess (Heads or tails): ").lower()

if user_guess == "tails" == computer_result:
    print("Good! You win")
    print(f"The computer's coin toss result was : {computer_result}")
elif user_guess == "heads" == computer_result:
    print("Good! You win")
    print(f"The computer's coin toss result was : {computer_result}")
elif user_guess == "tails" != computer_result:
    print("Sorry! you lost")
    print(f"The computer's coin toss result was: {computer_result}")
elif user_guess == "heads" != computer_result:
    print("Sorry! you lost")
    print(f"The computer's coin toss result was: {computer_result}")
else:
    print("invaild answer...")

# Review the lists
    
friends = ["example", "code", "python", "programming"]
# if I would to change any of these names in the lists, simpily I do this
friends[0] = "islam"
print(friends)
print(friends[:3])
print(friends[2:])

# Review the loop & while

i = 1 
while i <= 100:
    print(i)
    i += 1
    # same i = i+1
else:
    print("the condition is not true")
print("the loop has ended")

# another task
y = 1
while y <= 10:
    y += 1
    if y == 6:
        continue
    print(y)

# another task
y = 1
while y <= 10:
    y += 1
    if y == 6:
        break
    print(y)
print("the loop has ended")

# review the episode 51:
# the project after some abbreviation
list = []
names = input("Enter the first and last name of your friends: ").split(", ")
for name in names:
    name_parts = name.split()
    print(name_parts)
    first_name = name_parts[0][0]
    last_name = name_parts[1][0]
    abbreviation = first_name + "." + last_name + "."
    list.append(abbreviation)
print("Abbreviated Names: ")
for x in list:
    print(x)
# the second project:
sentence = input("Enter a sentence: ").split()
inverted_words = (sentence[-1:-7:-1])
print(inverted_words)
inverted_sentence = " ".join(inverted_words)
print("Reserved sentence:", inverted_sentence)
# the third project
import string
sentence = input("Please type a sentence with punctuations or any symbol: ")
new_sentence = " "
for x in sentence:
    if x not in string.punctuation:
        new_sentence += x
print("\n\n *** Here is the same sentence without punctuation *** \n\n", new_sentence)
# the forth project
import random
real_number = random.randint(0, 11)
guess_number = int(input("Guess a number between 1 and 10: "))
while guess_number != real_number:
    if guess_number < real_number:
        guess_number = int(input("Too low! Guess again: "))
    else:
        guess_number = int(input("Too high! Guess again: "))
print("Congratulations You guesed the number!")

