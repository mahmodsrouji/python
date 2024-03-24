print('Hello, wourld')
print("print('Hello, wourld')")
print('I love python \n Python is very easy\nThis is a new line')
print('Hello' + " " + 'there')
user_name = input("what is your name?\n")
print("Nice to meet you, " + user_name)
print( len (user_name))
user_PIN = input("What is your PIN number? \n")
print(type (user_PIN))
#another chapter
print('Octucode' [2])
#another thing
PIN_number = (input("Enter your PIN number: \n"))
print(len (PIN_number))
#another thing,This is the order, if I forget the type of the variable in which I know the value
print( type (3))
print( type ("3"))
print( type (False))
print( type (4.2))
user_PIN = input("What is your PIN number? \n")
print(type (user_PIN))

#another task, in the episode 15 

numbers = input("please enter three digits : \n")
first_number = int(numbers[0])
second_number = int(numbers[1])
third_number =int(numbers[2])
print(first_number+second_number+third_number)

#another task

str_length = input("please type length: \n")
str_width = input("please type width: \n")
length = float(str_length)
width = float(str_width)
area = length * width
str_area = str(area)
str_final_amount = input("How much for 1 meter? \n")
float_final_amount = float(str_area) * float(str_final_amount)
final_result = str(float_final_amount)
print("The total area is: " + str_area)
print("Give the guy:", final_result)
#or print("Give the guy: "  +  final_result)

#in an easier way

str_length = input("Please type length: \n")
str_width = input("please type width: \n")
str_price = input("How much for 1 meter? \n")
#convert type
length = float(str_length)
width = float(str_width)
price = float(str_price)

area = length * width
total_price = price * area

str_area = str(area)
str_total_price = str(total_price)

print("The total arae is: " + str_area)
print("Give the guy: $" + str_total_price)


#another task episode 17
total_seconds = input("Please type the number of seconds: \n")
int_seconds = int(total_seconds)
hours = int_seconds // 3600
minutes = (int_seconds % 3600) // 60
remaining_seconds = int_seconds % 60
print("This course is:", str(hours), "hours and", str(minutes), "minutes and", str(remaining_seconds), "seconds long")
#"or" print("This course is: " + str(hours) + " hours and " + str(minutes) + " minutes and " + str(remaining_seconds) + " seconds long.")


#episode 18
age = input("How old are you? \n")
int_age = int(age)
current_year = 2024
born_in = (current_year - int_age)
str_born_in = str(born_in)
print("you were born in the year: " + str_born_in)


#the previously projects in short way

#the first one
numbers = input("please enter tow digits \n")
print(int(numbers[0]) + int(numbers[1]))
#the second one
length = float(input("please type length: \n"))
width = float(input("please type length: \n"))
price = float(input("How much for 1 meter: \n"))
print("the total area is: ", str(length * width))
print("Give the guy: $", length * width * price)
#the third project
seconds = int(input("Please type the number of seconds: \n"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"This course is: {hours} hours and {minutes} minutes and {remaining_seconds} seconds long.")
#the forth projects
age = int(input("How ald are you? \n"))
print(f"You were born in the year {2024 - age} ")


#episode 21
print("Welcome to my apllication.")
age = int(input("how old are you? \n"))
if age >= 12:
    print("Good, you can use the app")
else:
    print("Sorry, you connot use the app.")

#if there are more than two condition we use "elif"
number = float(input("Enter a nomber: \n"))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
#mine project
mark = float(input("Type the mark here to rate: \n"))
if mark == 100:
    print("This mark is an excellent grade!")  
elif mark >= 90:
    print("This mark is an excellent grade!")
elif mark >= 75:
    print("This mark is in a good grade!") 
elif mark >= 50:
    print("This mark is in an acceptable grade!")
elif mark < 50:
    print("you got an f grad!")
else:
    print("This number is not supported")


#episode 22

#My first homework project without helping!
First_password = int(input("Enter your password: \n"))
Second_password = int(input("Enter your password again to confirm: \n"))
if First_password == Second_password:
    print("The operation is done")
    The_password = int(input("please enter your password: \n"))
else:
    print("Sorry, Passwords do not match!")
if First_password == Second_password == The_password:
    print("Welcome to your account")
else:
    print("The password is incorrect!")
#it needs a slight modification!

#The project after modification.
First_password = int(input("Enter your password: \n"))
Second_password = int(input("Enter your password again to confirm: \n"))
if First_password == Second_password:
    print("The operation is done")
    The_password = int(input("please enter your password: \n"))
    if First_password == Second_password == The_password:
        print("Welcome to your account")
    else:
        print("The password is incorrect!")
else:
    print("Sorry, Passwords do not match!")

#my second project homework is done correctly with the help of Bing
words = {"Yes", "yes", "No", "no", "Maybe", "maybe"}
user_input = input("Enter one of the required words: \n")
if user_input in words:
    print("you are answerd correctly")
else:
    print("your answer is incorrect")

#the third project homework is done correctly in 5 minutes
number = float(input("Enter the correct ambiguous number: \n"))
if number == 7:
    print("The number ambiguous is correct.")
else:
    print("Sorry, the number is not correct")


#episode 23
#Repeat codes using the method of Ibrahim Adel

password = input("please enter your password: \n")
correct_password = "abc"
if password == correct_password:
    print("Welcome to the app")
else:
    print("sorry, you can't use the app")

#another code
typed = input("Please type (Yes), (No), or (Maybe) \n")
if typed == "yes":
    print (f"You typed {typed}")
elif typed == "no":
    print(f"you typed {typed}")
elif typed == "maybe":
    print(f"You typed {typed}")
else:
    print(f"You typed {typed}, which is not an option \nplease stick to the options")

#the last code
guessed = int(input("please guess a number: \n"))
correct_number = 7
if correct_number == 7:
    print("Good guess")
else:
    print(f"You guessed {guessed}, but yhe correct number is {correct_number}")


#episode 24
#A way to write code that accepts both upper and lower letters options
area = input("chose an area: (cario), (Alexandria), or (Tanta) ")
if area.lower() == "cario":
    print("You chose cario")
elif area.lower() == "tanta":
    print("Tanta is nice!")
elif area.lower() == "alexandria":
    print("Feels like summer!")
else:
    print(f"Sorry, {area} is not on our list!")
#another thing, we need to condense the words into  one line instead of several lines
#with "or"
area = input("chose an area: (cario), (Alexandria), or (Tanta) ")
if area.lower() == "cario" or area.lower() == "alexandria" or area.lower() == "tanta":
    print(f"{area} is on our list!")
else:
    print(f"Sorry, {area} is not on our list!")
#with "and"
#another example.
name = input("Please enter your name: \n")
password = input ("Please enter your name: \n")
if name.lower() == "mahmoud" and password == "hiThere":
    print("Welcome back!")
else:
    print("Sorry, wrong name or password")


#episode 24+25
age = int(input("How old are you? \n"))
if age >= 18:
    license = input("Do you have a license? Type (Yes) or (No) \n").lower()
    if license == "yes":
        print("You can drive as you wish")
    elif license == "no":
        print("Sorry, you cannot drive unlees you have a driving license!")
    else:
        print(f"Sorry you entery of {license} is not understood")
else:
    print("You cannot drive unless you are 18 with a driving license exclusively")

#another project
is_syrian = input("Are you syria type (Yes) or (No) \n").lower()
if is_syrian == "yes":
    print("Good, that the first step")
    is_18 = input("Are you above 18 type (yes) or (No)? \n").lower()
    if is_18 == "yes":
        print("You can have an ID")
    else:
        print("Sorry, you have to be 18 or older")
        print("Please try again when you are 18")
else:
    print("Sorry, a syrian ID gves only to syrians!")


#The project for the third Chapter.
print("""
Welcome to my island!
There are two doors in front of you. 🚪 a red door, and 🚪 a blue door.
""")
door = input("Which door do you want to open? \n").lower()
if door == "red":
    print("Great! now you entered a room.")
    gift = input("You found three boxes: 🎁 white, 🎁 black, 🎁 green. \n").lower()
    if gift == "white":
        print("Oops! you opened a box filled with snakes 🐍🐍🐍")
    elif gift == "black":
        print("Oops! you opened a door filled with spiders 🕷️🕸️🕷️🕸️🕷️🕸️")
    elif gift == "green":
        print("Congratulations! You found the treasure! 💰💰💰")
    else: 
        print("invalid choice 🤷‍♂️🤷‍♂️🤷‍♂️")
elif door == "blue":
    print("""
    Oops! You chose the crocodile door.
    Game over! 🐊🐊🐊
    """)
else:
    print("invalid choice 🤷‍♂️🤷‍♂️🤷‍♂️")


#episode 30
import random
my_random = random.randint(-5,5)
print(my_random)

import octucode
print(octucode.course)


#episode 31

#First, I must determine the type of module that I want to work on!
import random
#second,I must write the random sentence I want, along with the conditions, and add it to a variable.
PIN_number = random.randint(1000,9999)
#third, I want to put the number chosen by the user into a variable through the input statement, and convert the word to a number (int).
user_number = int(input("Enter a 4-digits pin number "))
#After that, there are one of three conditions with their orders:
#The first one, set a condition for the number that the user chose, whether it is four digits or not, while setting the “len” key to measure the length of the digits.
if len(str(user_number)) != 4:
    print("please enter 4 digits!")
#second condition, Whether the user's number matches the random number chosen by the computer.
elif PIN_number == user_number:
    print("success! PIN code matched")
#third condition, If the chosen number does not match the random number
else:
    print("Failure! PIN code number didn't match")
    print(f"The computer generated this PIN {PIN_number}")


#episode 33
#Coin toss project
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

if user_guess.lower() == computer_result.lower():
    print("Good! You win")
    print(f"The computer's coin toss result was : {computer_result}")
elif user_guess != computer_result:
    print("Sorry! you lost")
    print(f"The computer's coin toss result was: {computer_result}")
else:
    print("invaild answer...")
#Note: In this project, it is necessary to write the Python lines first and then add the commands. Commands cannot be added inside the Python lines.
    

#episode 34
favorite_friends = ["Moafak", "Omar", "Mohamad", "Abdullah", "yazan"]
print(favorite_friends [0])

print(f"The first name on our list is {favorite_friends[0]} and the last name on our list is {favorite_friends[-1]}")

surname1 = favorite_friends[0] = "Abu yazan"
surname2 = favorite_friends[2] = "Abu elyas"
print(f"I would like to name my first and third friends on the list by their surname like this {surname1} and {surname2}.")


#episode 35
color = []
color.append("red")
color.append("blue")
print(color)
#The first project is 
color = []
fav_color = input("Add the first color you like: ")
color.append(fav_color)
command = input("Do you want to add more colors? Yes, or No? ").lower()
if command == "yes":
    fav_color = input("Add another color to the list: ")
    color.append(fav_color)
    print(f"The colors you like are {color} ")
elif command == "no":
    print(f"The color you like is: {color}")
else:
    print("invaild answer! please type (Yes) or (No)")

#There is a mudule for combining two lists into one sentence!
class_a = ["Tom","Silia", "Samer", "farah"]
class_b = ["Andrew", "Hadi", "Tina", "Samar", "Jacks"]
class_a.extend(class_b)
print(class_a)
#or,If we want to keep each list separate from the others, we have two ways:
class_a = ["Tom","Silia", "Samer", "farah"]
class_b = ["Andrew", "Hadi", "Tina", "Samar", "Jacks"]
students = []
students.extend(class_a)
students.extend(class_b)
print(students)
#second way
class_a = ["Tom","Silia", "Samer", "farah"]
class_b = ["Andrew", "Hadi", "Tina", "Samar", "Jacks"]
students = class_a + class_b
print(students)

#made the project of the Episode 35 without helping!
my_library = []
book = input("Enter the name of a book you own: ")
my_library.append(book)
book = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if book:
    my_library.append(book)
    print(f"Your Library: {my_library}")
else:
    print(f"Your Library: {my_library}")
wishlist = []
wishbook = input("Enter the name of the book you wish to have in the future: ")
wishlist.append(wishbook)
wishbook = input("Enter the name of another book you wish to have (or press'Enter' to skip): ")
if wishbook:
    wishlist.append(wishbook)
    print(f"Your Wishlist: {wishlist}")
else:
    print(f"Your Wishlist: {wishlist}")
acq_wishlist = input("Enter the name of the book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if acq_wishlist:
    if acq_wishlist in wishlist:
        my_library.append(acq_wishlist)
        wishlist.remove(acq_wishlist)
        print(f"Updated Library: {my_library}")
        print(f"Updated Wishlist: {wishlist}")
    else:
        print(f"This book '{acq_wishlist}' is not in your Wishlist! ")     
else:
    print(f"Your Library: {my_library}")
    print(f"Your Wishlist: {wishlist}")
donate_book = input("Enter the name of the book form you library that you wish to donate or press 'Enter to skip): ")
if donate_book:
    if donate_book in my_library:
        my_library.remove(donate_book)
        print(f"Final Library after Donations: {my_library}")
    else:
        print(f"This book '{donate_book}' is not in your Library!")
else:
    print(f"Your Library still has: {my_library} ")

#episode 36 "Doing the graduation project for the fourth unit".

#There are many other ways to add vairiable on the same line, for example:
name = input("What's you name? ")
print("Hello", name,", nice to meet you")
name = input("What's your name? ")
print("Hello " + name + ", nice to meet you")
name = input("What's you name? ")
print(f"Hello {name}, nice to meet you")

#The project in ibrahim way.
#step 1: Setup
library = []
wishlist = []
#Step 2: Adding Inivdiual Books
book_name = input("Enter the name of a book you own: ")
library.append(book)
book_name = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if book_name:
    library.append(book)
    print("\nYour Library: ", library)
#Step 3: Managing the Wishlist 
book_name = input("Enter the name of the book you wish to have in the future: ")
wishlist.append(book_name)
book_name = input("Enter the name of another book you wish to have (or press'Enter' to skip): ")
if book_name:
    wishlist.append(book_name)
    print("\nYour Wishlist: ", wishlist)
#step 4: Merging Wishlist into Library
acquired_wishlist = input("Enter the name of the book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if acquired_wishlist in wishlist:
    my_library.append(acquired_wishlist)
    wishlist.remove(acquired_wishlist)
    print("\nUpdated Library:", library)
    print("Updated Wishlist: ", wishlist)
#Step 6: Donate books
donated_book = input("Enter the name of the book form you library that you wish to donate or press 'Enter to skip): ")
if donate_book in library:
    library.remove(donated_book)
print("\nFinal Library after Donations: ", library)


#ُEpisode 38, 39, The project in other way
import random
print("Welcom to 'whose wallet?'")
print("You will give me a list of name, and I will pick a person to pay")
name = input("If you're ready, enter the names separated by a comma ")
names = name.split(", ")
length = len(names) -1
random_number = random.randint(0,length)
random_person = names[random_number]
print(f"Please ask '{random_person}' to take his wallet out. Dinner is on him")

#in an easier way, and with a new method name "choice"
import random 
print("Welcome to 'whose wallest?' ")
print("You will give me a list of names, and I will pick a person to pay")
names = input("If you're ready, enter the names separated by commas ").split(", ")
print(f"Please ask '{random.choice(names) }' to take his wallet out. Dinner is on him")

#The project in only three lines!
import random 
print("Welcome to 'whose wallest?' \n You will give me a list of names, and I will pick a person to pay randomly")
print(f"Please ask '{random.choice(input("If you're ready, Enter the names separated by commas ").split(', '))} to take out his wallet. Dinner is on him! " )


#episode 40
basket = [["'Apples'", "'Bananas'"] , ["'Milk'", "'Water'"]]
basket2 = ["'Cake'", "'Candy'"]
basket.append(basket2)
print(basket)
#in a shorter way.
basket = [["'Apples'", "'Bananas'"] , ["'Milk'", "'Water'"]]
basket.append(["'Cake'", "'Candy'"])
print(basket)
#We have a new module named 'Insert' whose function is to add new texts to the list, but with the ability to specify the place.
books = ["Book2", "Book3", "Book5"]
books.insert(0,"Book1")
books.insert(3,"Book4")
#if I want to add the 'book6' in the last, we have to optins:
books.insert(5,"Book6")
books.append("Book6")
print(books)


#episode 41
basket = [["Apples", "Bananas"] , ["Milk", "Water"]]
print(basket)
basket[0].insert(0,"Oranges")
basket[0].insert(3,"Kiwis")
basket[1].insert(0,"Coffee")
basket[1].remove("Water")
basket[1].insert(2,"Tea")
basket.append([1, 2, 3])
input("Press enter to vhange the contect .....")
print("Here is the updated basket")
print(basket)


#episode 42
#made the project of the "rabbit"
print("Welocme to place the rabbit\n")
field = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere should the rabbit go?")
position = (input("Please choose a row and a colmun "))
row = int(position[0])
colmun = int(position[1])
field[row-1][colmun-1] = "🐇"
print("\n Success .....\n")
print(f"{field[0]} \n{field[1]} \n{field[2]}")


#episode 43
#The project of the game "Rock, Paper, Scissors" in my way.

#Steps for writing a rock-paper-scissors project:
#1- Write the print command to present the game.
#2- Create an input to ask the user about the rules of the game, and put it in the (help) variable.
#3- put a conditional command (if conditional). If the user puts a helping word, we give him the rules.
#4- write a question input to choose between one of the three options, and put it in a variable (choice).
#5- Import randomness command.
#6- Use the "randint" module, put numbers from one to three, then use the if conditional to add a command between one of the options and put them in a variable.
#7-Put pictures of hands in a variable for each one of them.
#8-Use the "if conditional" to match the computer and the user choice, and write the final result in the print command.
#✊✌️🖐️
print("Welcome to the Rock, Paper, Scissors game:")
help = input("Press Enter to continue or type (Help) for the rules ").lower()
if help == "help":
    print("""
                 ********* RULES *********     
          1) You choose and the computer chooses 
          2) Rock smashes Scissors -> Rock wins
          3) Scissors cut Paper -> Scissors win
          4) Paper covers Rock -> Paper wins
""")
    choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

import random
if random.randint(1,3) == 1:
    computer = "Rock"
elif random.randint(1,3) == 2:
    computer = "Paper"
else:
    computer = "Scissors"

Rock = "✊"
Paper = "🖐️"
Scissors = "✌️"

if computer == choice:
    print(f"You chose: \n{choice}")
    print(f"Computer chose: \n{computer}")
    print("You got even!")

elif computer == "Rock" and choice == "Paper":
    print(f"You chose: \n{Paper}")
    print(f"Computer chose: \n{Rock}")
    print("You win paper cover Rock")
elif computer == "Rock" and choice == "Scissors":
    print(f"You chose: \n{Scissors}")
    print(f"Computer chose: \n{Rock}")
    print("You lost! Rock smashes Scissors")
elif computer == "Paper" and choice == "Rock":
    print(f"You chose: \n{Rock}")
    print(f"Computer chose: \n{Paper}")
    print("You lost! Paper cover Rock")
elif computer == "Paper" and choice == "Scissors":
    print(f"You chose: \n{Scissors}")
    print(f"Computer chose: \n{Paper}")
    print("You win! Scissors cut Paper")
elif computer == "Scissors" and choice == "Rock":
    print(f"You chose: \n{Rock}")
    print(f"Computer chose: \n{Scissors}")
    print("You win! Rock smashes Scissors")
elif computer == "Scissors" and choice == "Paper":
    print(f"You chose: \n{Paper}")
    print(f"Computer chose: \n{Scissors}")
    print("You lost! Scissors cut Paper")

else:
    print("Invaild answer! Please chose one of these options (Rock, Paper, Scissors)")


#episode 44 
#The project of the game "rock, Paper, Scissors" in the way of ibrahim.

import random
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("\nWelcom to the Rock, Paper, Scissors game:")
confirm = input("Press Enter to continue or type (Help) for the rules ").lower()
if confirm == "help":
    print("""
                 ********* RULES *********     
          1) You choose and the computer chooses 
          2) Rock smashes Scissors -> Rock wins
          3) Scissors cut Paper -> Scissors win
          4) Paper covers Rock -> Paper wins
""")
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invaild choice. Please run the program again and choose rock, paper, or scissors.")
# Display user choice in ASCII
else:
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nYou chose\n{paper_ascii}")
    else:
        print(f"\nYou chose\n{scissors_ascii}")
# Computer choice
computer_choice = random.choice(["rock", "paper", "scissors"])
if computer_choice == "rock":
    print(f"Computer chose:\n{rock_ascii} ")
elif computer_choice == "paper":
    print(f"Computer chose:\n{paper_ascii}")
else:
    print(f"Computer chose:\n{scissors_ascii}")
# Determine the Winner
if user_choice == computer_choice:
    print("It's a tie")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
     or
    (user_choice == "paper" and computer_choice == "rock")
     or
    (user_choice == "scissors" and computer_choice == "paper")):
   print(f"You win! {user_choice} beats {computer_choice}.") 
else:
    print(f"You lose! {computer_choice} beats {user_choice}.")


# episode 46
colors = ["Red", "Blue", "Green", "Yellow"]
for y in colors:
    if y == "Blue":
        print(f"{y} This is my favorite color!")
    else:
        print (y)
#pracice ...
friends = ["Abu Yazan", "Abu Lias", "Abu Talal", "Abu Basher"]
for x in friends:
    if x == "Abu Lias":
        print(f"{x} This is my relative ")
    elif x == "Abu Yazan":
        print(f"{x} This is my cousin")
    else:
        print(x)
# The projecrt of the the episode is:
numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if x % 2 == 0:
        print(f"\n{x}")
print("\nFinished the loop successfully")


# episode 47
attendees = ["Alice", "Bob", "Charlie"]
for person in attendees:
    print(person)
    commond = input("Is this person attending? (yes/no): ")
    if commond == "yes":
        print("Attendance Confirmed!")
    else:
        print("Attendeance not confirmed!")
        print("-----")

names = input("Enter the names of attendees separated by commas: ").split(", ")
for name in names:
    print(name)
    commond = input("Is this person attending? (yes/no): ")
    if commond == "yes":
        print("Attendance Confirmed!")
    else:
        print("Attendeance not confirmed!")
        print("-----")


