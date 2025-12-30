# AI-Powered Daily Planner
# Initially planner is empty
planner = []

# Function to add/create a new task
def create_task():
    task_name = input("Task name: ")

    if task_name == "": # Empty task name condition
        print("Task name cannot be empty.")
        return

    # Replacing (Something other than integer or empty) valueerror with try-except
    try: 
        days_left = int(input("Days left to complete: ")) 
        priority_score = int(input("Priority score (1-10): "))
    except ValueError:
        print("Please enter numeric values only.")
        return
    
    # Priority score validation
    if days_left <= 1 and priority_score >= 7:
        task_level = "Urgent"
    elif days_left <= 4 and priority_score >= 4:
        task_level = "Important"
    else:
        task_level = "Normal"

    # Adding task to planner using dictionary
    planner.append({
        "name": task_name,
        "days": days_left,
        "score": priority_score,
        "level": task_level
    })

    print("Task has been added to your planner.")



# Function to show all tasks
def display_planner():
    if not planner: # Check if planner is empty
        print("Your planner is empty.")
        return

    print("--- Task Overview ---\n") # Planner menu
    for i in range(len(planner)):
        j = planner[i]
        print(f"{i+1}. {j['name']} | {j['level']} | Due in {j['days']} day(s)")



# Main menu loop
while True: # Always true condition
    print("*** Smart Daily Planner ***")
    print("A - Add Task")
    print("V - View Planner")
    print("E - Exit")

    user_choice = input("Select an option: ").upper() # Make sure the letter is uppercase

    if user_choice == "A":
        create_task()
    elif user_choice == "V":
        display_planner()
    elif user_choice == "E":
        print("Planner closed. Goodbye!")
        break
    else:
        print("Invalid selection, Please choose again.")
