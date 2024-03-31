# the episode 48:
done_tasks = []
ongoing_tasks = []
tasks = input("Enter your tasks for today: ").split(", ")
for task in tasks:
    done = input(f"Did you finish {task} alredy? ").lower()
    if done == "yes":
        print("Nice Job")
        done_tasks.append(task)
    else:
        print("Try not to put it off")
        ongoing_tasks.append(task)
    print("------------")
progress = input("Do you want to see your today's progress?(yes, no)\n").lower()
if progress == "yes":
    print("\n******** Done Tasks ********\n")
    print(done_tasks)
    print("\n****** Ongoing Tasks ******\n")
    print(ongoing_tasks)
else:
    input("Please hit Enter to exit ")