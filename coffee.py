import time
from cofe import CoffeeMachine

try:
    
    coffee = CoffeeMachine(100,100,100)
    while True:
        choice = input("\nWhat you feeling today..?\nEspresso/Cappuccino/Latte: ")
        if choice.lower() == "espresso":
            coffee.dispense("espresso")

        if choice.lower() == "cappuccino":
            coffee.dispense("cappuccino")

        if choice.lower() == "latte":
            coffee.dispense("latte")

        if choice.lower() == "off":
            print("Powering Off...")
            time.sleep(1)
            break

        if choice.lower() == "refil":
            coffee.refil()

        if choice.lower() == "report":
            print("\n---Todays report---")
            r = coffee.report()
            print("Water: ",r[0],"ml",sep="")
            print("Milk: ",r[1],"ml",sep="")
            print("Coffee: ",r[2],"gm",sep="")
            print("Money: Rs.",r[3],sep="")
            print("Sales: ",r[4],sep="")

except ValueError:
    print("Enter details Correctly")