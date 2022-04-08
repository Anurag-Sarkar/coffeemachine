import time
class CoffeeMachine:

        def __init__(self,water,milk,coffee):
            self.__water = water
            self.__milk = milk
            self.__coffee = coffee
            self.__money = 0
            self.__sale = 0

        def refil(self):
            c = input("Default of Custom Refil: ")
            if c.lower() == "default":
                self.__water += 500
                self.__milk += 500
                self.__coffee += 500
            elif c.lower() == "custom":
                self.__water += int(input("Water: "))
                self.__milk += int(input("Milk: "))
                self.__coffee += int(input("Coffee: "))
            else:
                print("Pardon?")    
            print("Refil Successfull!")
                

        def report(self):
            if self.__water < 0 and self.__milk < 0 and self.__coffee < 0:
                self.__water = 0
                self.__milk = 0
                self.__coffee = 0  
            return self.__water,self.__milk,self.__coffee,self.__money,self.__sale
        
        def dispense(self,order):
            if order.lower() == "espresso":
                if self.__water >= 50 and self.__milk >= 100 and self.__coffee >= 20:
                    i = 0
                    money = int(input("It will be Rs.200: "))
                    if money == 200:
                        print("Preparing Your order...")
                        time.sleep(3)
                        print("Here's Your Espresso... Enjoy!")
                        print()
                        self.__water -= 50
                        self.__milk -= 100
                        self.__coffee -= 20
                        self.__money += 200
                    if money >= 200:
                        print("Preparing Your order...")
                        time.sleep(3)
                        print("Here's Your Espresso... Enjoy!")
                        if money > 200:
                            print(f"Your Change Rs.{money-200} ")
                        self.__water -= 50
                        self.__milk -= 100
                        self.__coffee -= 20
                        self.__money += 200
                        self.__sale += 1
                    while money < 200:
                        if money < 200:
                            diff = 200-money
                            print("We need Rs.",diff,"more")
                            m = int(input())
                            money += m
                        if money >= 200:
                            print("Preparing Your order...")
                            time.sleep(3)
                            print("Here's Your Espresso... Enjoy!")
                            if money > 200:
                                print(f"Your Change Rs.{money-200} ")
                            self.__water -= 50
                            self.__milk -= 100
                            self.__coffee -= 20
                            self.__money += 200
                            self.__sale += 1
                        if i == 2:
                            print("Sorry we cant provide coffee to chindi!!!")
                            break
                        i+=1
                else:
                    print("Sorry, There is not much resource to prepare your order!!!")

            if order.lower() == "cappuccino":
                if self.__water >= 50 and self.__milk >= 100 and self.__coffee >= 20:
                    i = 0
                    money = int(input("It will be Rs.300: "))
                    if money == 300:
                        print("Preparing Your order...")
                        time.sleep(3)
                        print("Here's Your Cappuccino... Enjoy!")
                        print()
                        self.__water -= 50
                        self.__milk -= 100
                        self.__coffee -= 20
                        self.__money += 300
                    if money >= 300:
                            print("Preparing Your order...")
                            time.sleep(3)
                            print("Here's Your Cappuccion... Enjoy!")
                            if money > 300:
                                print(f"Your Change Rs.{money-300} ")
                            self.__water -= 50
                            self.__milk -= 100
                            self.__coffee -= 20
                            self.__money += 300
                            self.__sale += 1

                    while money < 300:
                        if money < 300:
                            diff = 300-money
                            print("We need Rs.",diff,"more")
                            m = int(input())
                            money += m
                        if money >= 300:
                            print("Preparing Your order...")
                            time.sleep(3)
                            print("Here's Your Cappuccion... Enjoy!")
                            if money > 300:
                                print(f"Your Change Rs.{money - 300} ")
                            self.__water -= 50
                            self.__milk -= 100
                            self.__coffee -= 20
                            self.__money += 300
                            self.__sale += 1
                        if i == 2:
                            print("Sorry we cant provide coffee to chindi!!!")
                            break
                        i+=1
                else:
                    print("Sorry, There is not much resource to prepare your order!!!")
                
            if order.lower() == "latte":
                if self.__water >= 50 and self.__milk >= 100 and self.__coffee >= 20:
                    i = 0
                    money = int(input("It will be Rs.150: "))
                    if money == 150:
                        print("Preparing Your order...")
                        time.sleep(3)
                        print("Here's Your Latte... Enjoy!")
                        print()
                        self.__water -= 50
                        self.__milk -= 100
                        self.__coffee -= 20
                        self.__money += 150
                    elif money >= 150:
                            print("Preparing Your order...")
                            time.sleep(3)
                            print("Here's Your Latte... Enjoy!")
                            if money > 150:
                                print(f"Your Change Rs.{money-150} ")
                            self.__water -= 50
                            self.__milk -= 100
                            self.__coffee -= 20
                            self.__money += 150
                            self.__sale += 1
                    while money < 150:
                        if money < 150:
                            diff = 150-money
                            print("We need Rs.",diff,"more")
                            m = int(input())
                            money += m
                        if money == 150:
                            print("Preparing Your order...")
                            time.sleep(3)
                            print("Here's Your Latte... Enjoy!")   
                            if money > 150:
                                print(f"Your Change Rs.{money-150} ")                         
                            self.__water -= 50
                            self.__milk -= 100
                            self.__coffee -= 20
                            self.__money += 150
                            self.__sale += 1
                        if i == 2:
                            print("Sorry we cant provide coffee to chindi!!!")
                            break
                        i+=1
                else:
                    print("Sorry, There is not much resource to prepare your order!!!")
