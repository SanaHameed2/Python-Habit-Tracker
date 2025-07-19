# Simple Habit Tracker with Visual Aid

# Step 1: Initialize an empty list to store habits
habits = []

# Step 2: Function to add a habit
def add_habit(name):
    habit = {"name": name, "done_today": False}
    habits.append(habit)
    print(f"✅ Habit '{name}' added.\n")

# Step 3: Function to show all habits
def show_habits():
    print("\nYour Habits:")
    if not habits:
        print("No habits added yet.\n")
    else:
        for index, habit in enumerate(habits):
            status = "✅" if habit["done_today"] else "❌"
            print(f"{index + 1}. {habit['name']} - {status}")
    print()

# Step 4: Function to mark a habit as done
def mark_done():
    show_habits()
    if not habits:
        return
    
    try:
        choice = int(input("Enter the number of the habit you completed: "))
        if 1 <= choice <= len(habits):
            habits[choice - 1]["done_today"] = True
            print(f"✅ Marked '{habits[choice - 1]['name']}' as done!\n")
        else:
            print("❌ Invalid habit number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Step 5: Main loop
while True:
    print("What would you like to do?")
    print("1. Add a new habit")
    print("2. Mark a habit as done")
    print("3. Show all habits")
    print("4. Exit\n")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the name of the habit: ")
        add_habit(name)
    elif choice == "2":
        mark_done()
    elif choice == "3":
        show_habits()
    elif choice == "4":
        print("👋 Exiting Habit Tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")
