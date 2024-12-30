"""
 Naomi Clark
 Module 08 Lab Assignment
 Part B
 
 This program creates a task class for a to-do list application and a createTask() function that creates and adds tasks to a to-do list.
 """


class Task:
    def __init__(self, task_name, completion):
        self.task_name = task_name
        self.completion = completion

    def appendFile(self, task_name, completion):
        f = open("todo-list.txt", "a")
        f.write(f"Task Name: {task_name}\n")
        f.write(f"Task Complete: {completion}")
        f.write(f"\n\n")
        f.close()


def createTask():
    try:
        task_name = input("Task Name: ")
        completion = input("Task Complete? Yes/No: ")

        if (completion.lower() != "yes") and (completion.lower() != "no"):
            raise ValueError
        else:
            return task_name, completion
    except ValueError:
        print("You must enter either 'Yes' or 'No'")


try:
    add_task = input("Want to add a task? Yes/No: ")
    if (add_task.lower() != "yes") and (add_task.lower() != "no"):
        raise ValueError
    else:
        while add_task.lower() == "yes":
            task_name, completion = createTask()
            new_task = Task(task_name, completion)
            new_task.appendFile(task_name, completion)
            add_task = input("Want to add a task? Yes/No: ")

except ValueError:
    print("You must enter either 'Yes' or 'No'")
