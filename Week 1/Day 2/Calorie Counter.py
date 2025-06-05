totalcalories = 0
totalprotein = 0
print("Hey i am your new calorie counter, created by a complete rookie but hey you get what you pay for")
caloricallowance = int(input("Whats your caloric allowence today? "))
proteingoal = int(input("Whats your protein goal"))
print(f"\nok so your calorie goal is {caloricallowance} and your protein goal is {proteingoal}g")

mealtotal = int(input("\n\n\nOk then since we know that how many meals did you eat today? "))
for i in range(mealtotal):
    print(f"\n Meal {i + 1}")
    calories = int(input('How many calories? '))
    protein = int(input("How many grams of protein?"))
    totalcalories += calories
    totalprotein += protein

if caloricallowance == totalcalories:
    print("your dead on track for calories, keep it up!")
if caloricallowance > totalcalories:
    caloricdifference = caloricallowance - totalcalories
    print(f"You haven't hit your calorie, go eat something now \n You need to consume {caloricdifference} more!")
if totalcalories > caloricallowance:
    caloricdifference = totalcalories - caloricallowance
    print(f"You have gone over your calories by {caloricdifference}")
if totalprotein == proteingoal:
    print("your protein is bang on Good Job!")
if totalprotein > proteingoal:
    proteindifference = totalprotein - proteingoal
    print(f"damn you flew over that target by {proteindifference}")
if totalprotein < proteingoal:
    proteindifference = proteingoal - totalprotein
    print(f"your only {proteindifference}g behind, get that ate")
