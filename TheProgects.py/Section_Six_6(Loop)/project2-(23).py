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
    print("\n"+name+"\n")
    commond = input("Is this person attending? (yes/no): ")
    if commond == "yes":
        print("Attendance Confirmed!")
    else:
        print("Attendeance not confirmed!")
        print("-----")
# another project.
travel_list = input("Please type the names of the countries: ").split(", ")
for country in  travel_list:
    print(f"\n{country}\n")
    visited = input(f"Have you ever visited {country} before? (yes,no)\n").lower()
    if visited == "yes":
        print("I hope you had a wonderful time \n")
    else:
        print("I hope you get to visit it soon \n")
    print("------")
input("Press enter to exit.....")