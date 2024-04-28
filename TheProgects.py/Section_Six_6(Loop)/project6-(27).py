# The episode 50:
numbers = [1,2,3,4,5]
total = 0 
print("Let's add each number to the next")
for i in numbers:
    total += i
    print(f"-> {total}")
    print(f"\nThe total number is: {total}\n")

# Some informations.
name = "Ibrahim"
print("\n".join(name))
names = ["Ibrahim", "Ben", "Cherry", "Decken", "Emily", "Samer", "Ali"]
print(" \U0001F449 ".join(names))
print(names[0:4])
print(names[0:5:2])
print(names[0:7:2])