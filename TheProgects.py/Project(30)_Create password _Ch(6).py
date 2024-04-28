import random 
import string
print("Welcome to the password Generator!")
length = int(input("Enter the total number of characters in the password: "))
letters = int(input("Enter the number of letters in the password: "))
numbers = int(input("Enter the number of numbers in the password: "))
symbols = int(input("Enter the number of symbols in the password: "))
if length != letters + numbers + symbols:
    print("invaild input. The sum of letters, numbers, and symbols doesn't match the password")
else:
    A = random.choices(string.ascii_letters, k=letters)
    B = random.choices(string.digits, k=numbers)
    c = random.choices(string.punctuation, k=symbols)
    shuffle = A + B + c
    random.shuffle(shuffle)
    password = ''.join(shuffle)
    print(f"Generated Password: {password}")