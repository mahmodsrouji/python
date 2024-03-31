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