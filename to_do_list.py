x = "Add your tasks here".center(100,"-")
print(x)

txt = '''
Press 1 to add tasks.
Press 2 to view tasks.
Press 3 to delete tasks.
Press 4 to update task.
Press 5 to exit.
'''
print(txt)

task_list = []



while True:

    response = int(input("Enter your command: "))

    i = 0

    if(response == 1):

        num = int(input("Enter number of tasks to add: "))

        for i in range(1,num+1):
            task = input(f"Enter task {i}: ")
            task_list.append(task)

        print("Tasks have beem added to list\n")

    elif(response == 2):
   
        if(len(task_list)==0):
           print("There is no task\n")

        else:
            while i<len(task_list):
                print(f"Task {i+1}: {task_list[i]}")
                i = i+1


    elif(response == 3):
        
        index = int(input("Task to delete: "))

        task_list.pop(index-1)

        print("Task has been deleted successfully.")

    elif(response == 4):
        index = int(input("Task to update: "))

        changes = input(f"Update task {index}: ")

        task_list[index-1] = changes

        print("Task has been updated")
    
    elif(response == 5):
        break