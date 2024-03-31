# The project in only three lines!
import random 
print("Welcome to 'whose wallest?' \n You will give me a list of names, and I will pick a person to pay randomly")
print(f"Please ask '{random.choice(input("If you're ready, Enter the names separated by commas ").split(', '))} to take out his wallet. Dinner is on him! " )


name1 = input("If you're ready, Enter the names separated by commas ").split(', ')
print(name1)
split = "test. test2. test 3".split(". ")
print(split)
names = ['1', '3', '5']
output = random.choice(split)
print(output)

print("The dinner is on " + random.choice(input(f"Welocme to 'whose wallest? \n You will give me a list of names, and I will pick a person to pay randomly \n Enter the names seperated by commas: ").split(', ')))


def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(int(input("enter number 1: ")), int(input("enter number 2: ")))
print("The result is", result)

# Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)