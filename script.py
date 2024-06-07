# Todo App
# Display Initial Info To User
print("Welcome To Your To Do App")
#Logic For All Inputs
def addtask():
    with open("tasks.txt",'r+') as f:
        indextask = len(f.readlines()) + 1
        f.write(f"{indextask}-{newtask}\n")
        print(f"Your task is at index: {indextask}")
def viewfiles():
    with open("tasks.txt") as f:
        print(f.readlines())
def deletetask():
    with open("tasks.txt") as f:
        tasks=f.readlines()
        if  0 < indextoremove <= len(tasks):
            tasks.pop(indextoremove - 1)
            with open("tasks.txt", 'w') as f:
                for index, task in enumerate(tasks):
                    task_text = task.split('-', 1)[1]
                    f.write(f"{index + 1}-{task_text}")
            print("Task removed successfully")
        else:
            print("Invalid task index")
# Input Logic
while True:
    userinput= int(input("What action would you like to perform? 1-Add A Task, 2-View All Tasks, 3-Remove A Task, 4-Quit: "))
    if userinput == 1:
        print("User would like to add a new task to the list\n")
        print("Starting Query\n")
        newtask = input("Kindly input the task to add to the todo list: ")
        addtask()
    elif userinput == 2:
        print("User would like to view all tasks in their list")
        print("Starting Query")
        viewfiles()
    elif userinput == 3:
        print("User would like to remove a task")
        print("Staritng query")
        viewfiles()
        indextoremove = int(input("At what index is the task you want to remove? "))
        deletetask()
    elif userinput == 4:
        print("Quiting the application")
        break
    else:
        print("That isn't a valid input, Try again")
