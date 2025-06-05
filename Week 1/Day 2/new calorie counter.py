print("Hey, I am your calorie counter for today, please first give me some details")
#Getting details
meals = []
name =  []
totalprotein = 0
totalcalories = 0
name = input("Whats your name?\n".capitalize().strip())
name = name.capitalize()
caloriegoal = int(input(f"and how many calories are you aiming to consume today {name}"))
proteingoal = int(input(f"Ok {name}, since you are looking at {caloriegoal} calories, how many grams of protein are you looking to pack into that"))
weight = int(input("And how many Lbs do you weigh?"))
idealprotein = weight*1
#if statement to avoid protein defficiency
if proteingoal < idealprotein:
    print(f"{name} that protein goal is looking a little low, may I reccomend that you up that too {idealprotein}?")
    answer1 = input("yes/no".strip().lower())
    validresponse1 = ["yes", "no"]
    if answer1 not in validresponse1:
        print("dude I gave you one job...")
        exit()
    elif answer1 == "yes":
        proteingoal = idealprotein
        print(f"Ok {name}, I have updated your protein goal to {proteingoal}g")
    else: 
        print("Your the boss")
elif proteingoal > idealprotein:
    print("Thats alotta protein, your poor bowels...")
#How many meals 
numofmeals = int(input(f"Ok {name}, how amy meals are we having today? "))
for i in range(numofmeals):
    mealname = input(f"Whats meal {i+1} called?".strip().capitalize())
    ingredients = input(f"Ok what was in {mealname}?")
    calories = int(input("and how many calories?"))
    protein = int(input("how many grams of protein? "))
    meals.append({"name":mealname, "calories": calories, 'protein': protein, "ingredients": ingredients})
#listing meals to user
for meal in meals:
    print(f"Meal - {meal["name"]}:\nDescription {meal["ingredients"]}\nCalories - {meal["calories"]}):\nProtein - {meal["protein"]}g")
    totalcalories += calories
    totalprotein += protein
#calorie and protein goal vs actual
if totalcalories > caloriegoal:
    print(f"You went over your calories by {totalcalories-caloriegoal}calories")
elif caloriegoal > totalcalories:
    print(f"You were {caloriegoal-totalcalories} under calories")
else:
    print("Good Job! You were bang on calories")
if totalprotein > proteingoal:
    print(f"GREAT JOB you smashed that protein like it owed you money")
elif proteingoal > totalprotein:
    print(f"You were under protein by {proteingoal-totalprotein}grams")
else:
    print("You were spot on with your protein buddy")

    


