#episode 42
#made the project of the "rabbit"
print("Welocme to place the rabbit\n")
field = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print("\nWhere should the rabbit go? 🐇 ")
print(f"\n{field[0]} \n{field[1]} \n{field[2]}\n")
position = (input("Please choose a row and a colmun: "))
row = int(position[0])
colmun = int(position[1])
field[row-1][colmun-1] = "🐇"
print("\n Success .....\n")
print(f"{field[0]} \n{field[1]} \n{field[2]}")