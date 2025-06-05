score = 0 
maxscore = 30
correctanswer2 = "skyrim"
correctanswer3 = ["south shields", "computer"]
correctanswer4 = "nicotine pouches"
print('Well Hello there, I have a quiz')
answer1 = input('Do you want to take it? (yes/no) '.strip().lower())
validanswer1 = ["yes", "no", "bannana"]
if answer1 not in validanswer1:
    print('Oi did I not just tell you how to answer?')
elif answer1 == "yes":
    #ANSWER2
    print("Great, heres question one")
    answer2 = input('Whats my current fave video game? '.strip().lower())
    if answer2 not in correctanswer2:
        print('Nope the correct answer is ', correctanswer2)
    else:
        print("DING DING DING 10 POINTS")
        score = score+10
        print('Your current score is, ',score)
    print("Let's Continue....")
    #ANSWER3
    answer3 = input("Where was i coded".strip().lower())
    if answer3 not in correctanswer3:
        print('Nah bro but nice try')
    elif answer3 == "south shields":
        print("Correct")
        score = score+10
    else:
        print("How funny but fair")
        score = score+5
    print("Next question")
    #ANSWER4
    answer4 = input("Whats my preferred method of nicotine? ".strip().lower())
    if answer4 not in correctanswer4:
        print("Nope its actually", correctanswer4)
    else:
        print("DING DING DING")
        score = score+10
    print("Your score was ",score,"/30")
                           
if answer1 == "bannana":
    print("You found my bannana")
else:
    print("Bye")
