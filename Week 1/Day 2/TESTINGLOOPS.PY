moneyspent = 0
print('Hi I am your spending tracker')
trips = int(input("How many times did you go to the shops today? "))
for l in range(trips):
    print(f"\nShop Trip {l + 1}")
    moneyspent += int(input("how much did you spend to the nearest £?"))
    
print("So overall you spent £", moneyspent)
