#Intro
print('Hello, I have a few questions')
#Getting name
print('Whats your name')
name = input(str)
#Getting age
print("Nice to meet you ",name," how old are you?")
age = int(input())
#Confirmation
print("Ok so your name is ",name, "and you are ",age, "Years old")
agemonths = age*12
print("did you know that makes you",agemonths," in months?")
#True or False
response1 = input('Because im a silly goose please answer as either True or False   ').strip().lower()
validresponse = ["true", "false"]
if response1 not in validresponse:
    print("you had one job, dammit....")
elif response1 == "true":
    print("OIOI Smarty Pants")
else:
    print('Idiot...')




    