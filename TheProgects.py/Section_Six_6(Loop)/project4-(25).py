# Multiplication table project:
print("*** Welcome to the multiplication table ***")
number = int(input("Enter a number: "))
print(f"\nMultiplication table for {number:} \n")
for i in range (1,11):
    result = number * i
    print(f"{number} x {i} = {result}")