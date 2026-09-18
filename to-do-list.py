def task():
    tasks=[]
    print("___WELCOME TO THE TASK MANAGER APP___")
    total_task=int(input("Enter how many tasks you want to add = "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i}= ")
        tasks.append(task_name)
        print("today's tasks are in (tasks)")
    while True:
        operation=int(input("Enter 1=ADD\n 2=UPDATE\n 3=DELETE\n 4=VIEW\n 5=EXIT/stop/"))
        if operation == 1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"task {add} has been successfully added...")
        elif operation == 2:
            update_val = input("Enter the task you want to update = ")
            if update_val in tasks:
                up = input("Enter new the task = ") 
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"updated task {up}")
            else:
                print("NOT FOUND")
        elif operation == 3:
            del_val = input("Enter the task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"task {del_val} has been deleted...")
            else:
                print("NOT FOUND")
        elif operation == 4:
            print(f"total tasks = {tasks}")
        elif operation == 5:
            print("closing the program...")
            break
        else:
            print("invalid input")
task()               