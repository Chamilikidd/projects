#this is a task list
user = input("Welcome to our task manager, whats your name?")
tasks = [] #setting up base for dictionary
validpriorities = ["High", "Medium", "Low"]

#priorities high medium and low
#tasknames
#estimated times in mins
taskamount = int(input(print("How many tasks do we need to achieve today")))

for i in range(taskamount):
    taskname = input(f"What is the name of task {i+1}")
    taskpriority = input("What is the priority of this task (High, Medium or low)").strip()
    taskpriority = taskpriority.capitalize()
    time = int(input(print("How long will this take in mins?")))
    tasks.append({"name":taskname, "priority":taskpriority, "time":time })

#setting priorities
priority_order = {"High": 0, "Medium": 1, "Low": 2}
tasks.sort(key=lambda x: priority_order[x["priority"]])
for t in tasks:
    print(f"TASK - {t["name"]}\n PRIORITY - {t["priority"]}\n TIME - {t["time"]} mins")







    
