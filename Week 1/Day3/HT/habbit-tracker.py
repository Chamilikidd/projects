from datetime import datetime
import random

print("Hi there,")
 #collectiing and cleaning users name
username = input("Whats your name")
username = username.strip().capitalize()
#opening screen
c1 = "1 - Create a new habit"
c2 = "2 - View todays habits"
c3 = "3 - Mark a habit as complete"
c4 = "4 - Save Progress"
c5 = "5 - Exit"
habbits = []
priorityorder = {"High": 0, "Medium": 1, "Low": 2}
def prioritycatagory():
    global validpriority, priority
    validpriority = ["High", "Medium", "Low"]
    priority = input(f"High, Medium or Low priority?")
    priority = priority.capitalize().strip()
    if priority not in validpriority:
        print("Invalid response, please try again")
        prioritycatagory()

def completion():
    global HYC
    HYC = input("Have you completed a task? (Yes/No)")
    HYC = HYC.capitalize().strip()
    if HYC == "Yes":
        global NOH
        NOH = int(input("How many did you complete"))
        for t in range(NOH):
            for q in habbits:
                print(f"please select the habbit by unique ID\nName {q["name"]}\nID {q['habbitID']}")
                wid = int(input("Please enter the unique ID"))
                if wid == q["habbitID"]:
                    q['completed'] = True
 #creating opening CLI

def options():
    print(f"Ok {username}, what would you like to do today?\n{c1}\n{c2}\n{c3}\n{c4}\n{c5}")
    global validresponse, whatdo
    validresponse = ["1", "2", "3","4","5","6"]
    whatdo = input("Please select your number")
    whatdo = whatdo.strip()
    if whatdo not in validresponse:
        print("Invalid responce please select one of the following numbers")
        options()
    elif whatdo == "1":
        print(f"You have chosen {c1}")
        howmanyhabits = int(input("How many habits would you like to create?"))
        for i in range(howmanyhabits):
            habbitID = random.randint(1, 100000000)
            habitname = input(f"What is  the name of Habit {i + 1}")
            prioritycatagory()
            habbits.append({"name": habitname, "priority": priority, "created": datetime.now().strftime('%d/%m/%Y'), "habbitID": habbitID, "completed": None})
            habbits.sort(key=lambda x: priorityorder [x ["priority"]] )
        
    elif whatdo == "2":
        for h in habbits:
            status = "Complete" if h["completed"] else "To be complete"
            print(f"You have added \nName - {h["name"]} \n Priority - {h["priority"]}\n Date - {h["created"]} \n ID -{h["habbitID"]} \n{status}")
    

    elif whatdo == "3":
        completion()
    options()
options()