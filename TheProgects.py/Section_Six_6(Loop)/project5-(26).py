# The project of the episode 48 "my work":
items_list = []
price_list = []
print("***** Welcome to ishop calculator *****")
numbers = int(input("how many items are there in your basket today? "))
print("Let's get to counting them ....")
for n in range(numbers):
    items = input(f"Please tell me the name of the item number {n+1}: ")
    items_list.append(items)
    price = float(input(f"What is the price of {items}:\n$"))
    price_list.append(price)
command = input("Would you like to see your entire basket items? ").lower()
if command == "yes":
    print(items_list)
    command_2 = input("Would you like to see how much it'll cost? ").lower()
    if command_2 == "yes":
        print(f"\nBuying these items will cost:\n${sum(price_list)}")
    else:
        input("Press Enter to exit ")
else:
    command_2 = input("Would you like to see how much it'll cost? ").lower()
    if command_2 == "yes":
        print(f"\nBuying these items will cost:\n${sum(price_list)}")
    else:
        input("Press Enter to exit ")


# The episode 49:
# The same project of the ibrahim work:
items = []
prices = []
print("\n***** Welcome to ishop calculator *****\n")
number_of_items = int(input("how many items are there in your basket today? "))

if number_of_items > 0:
    print("\nLet's get to counting them ....")
    for i in range(0, number_of_items):
        name = input(f"Please tell me the name of the item number {i+1}: ")
        items.append(name)
        price = float(input(f"What is the price of {name}:\n$"))
        prices.append(price)

    choice = input("Would you like to see your entire basket items? ").lower()
    if choice == "yes":
        print(items)
        see_price = input("Would you like to see how much it'll cost? ").lower()  
        if see_price == "yes":
            print("\nBuying these items will cost:")
            print(sum(prices))
        else:
            input("Press Enter to exit")
    else:
        input("Press Enter to exit")
else:
    print("Seems like you're not in the mood for shopping today")