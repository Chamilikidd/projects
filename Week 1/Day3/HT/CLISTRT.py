#opening screen
c1 = "1 - Create a new habit"
c2 = "2 - View todays habits"
c3 = "3 - Mark a habit as complete"
c4 = "4 - Save Progress"
c5 = "5 - Exit"

def userinfo():
    print("Hi there,")
 #collectiing and cleaning users name
    global user
    user = input("Whats your name")
    user = user.strip().capitalize()
    
 #creating opening CLI

def options():
    print(f"Ok {user}, what would you like to do today?\n{c1}\n{c2}\n{c3}\n{c4}\n{c5}")
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
            
    
    


