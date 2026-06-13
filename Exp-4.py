#Coder:Aliya Shaikh
#Code for concepts of list

tasks=["banana","cherry","apple"]
print(f"Original tasks:", tasks)
#adding a task
add_task=input("enter the new task: ")
tasks.append(add_task)
print(f"tasks after adding:", tasks)
#removing a task
index=int(input("enter the index of the task to remove: "))
if 0<=index<len(tasks):
    removed_task=tasks.pop(index)
else:
    print("Invalid index")
print(f"tasks after removing:", tasks)
#update/edit a task
index=int(input("enter the index of the task to update: "))
if 0<=index<len(tasks):
    updated_task=input("enter the updated task: ")
    tasks[index]=updated_task
else:
    print("invalid index")
print(f"tasks after updating:", tasks)
#sort tasks
tasks.sort()
print(f"sorted tasks:", tasks)

"""
SAMPLE OUTPUT:
Original tasks: ['banana', 'cherry', 'apple']
enter the new task: guava
tasks after adding: ['banana', 'cherry', 'apple', 'guava']
enter the index of the task to remove: 2
tasks after removing: ['banana', 'cherry', 'guava']
enter the index of the task to update: 1
enter the updated task: kiwi
tasks after updating: ['banana', 'kiwi', 'guava']
sorted tasks: ['banana', 'guava', 'kiwi']
"""
