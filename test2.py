attendees = ["Alice", "Bob", "Charlie"]
for person in attendees:
    print(person)
    commond = input("Is this person attending? (yes/no): ")
    if commond == "yes":
        print("Attendance Confirmed!")
    else:
        print("Attendeance not confirmed!")
        print("-----")