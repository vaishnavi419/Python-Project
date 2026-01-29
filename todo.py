def to_do_list():
    tasks=[]
    while True:
        print("Add Task")
        print("Remove Task")
        print("Show Tasks")
        print("Quit")
        ch=input("Enter Your Choice:-");
        if ch == "1":
            task=input("Enter Task:-")
            tasks.append(task)
        elif ch=="2":
            task=input("Enter task to remove:-")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task Not found")
        elif ch=="3":
            print("Tasks");
            for task in tasks:
                print("-"+task)
        elif ch=="4":
            break
        else:
            print("Invalid choice")
to_do_list()


"""
Output:-

Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-1
Enter Task:-Breakfast
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-1
Enter Task:-Lunch
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-1
Enter Task:-Dinner
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-1
Enter Task:-Cooking
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-2
Enter task to remove:-Salad
Task Not found
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-2
Enter task to remove:-Cooking
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-3
Tasks
-Breakfast
-Lunch
-Dinner
Add Task
Remove Task
Show Tasks
Quit
Enter Your Choice:-4
"""