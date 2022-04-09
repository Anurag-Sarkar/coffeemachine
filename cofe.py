import time
import json
from pathlib import Path

class Money:
    def __init__(self):
        self.__money = 0
    
    def passmoney(self):
        return self.__money
    def takemoney(self,givenmoney,cost):
        i = 0
        if givenmoney == cost:
            self.__money += cost
            return True
        elif givenmoney < cost:
            while givenmoney < cost:
                if i == 3:
                    print("Nahi Khelna mujhe!!")
                    print("apne paise leke bhaag ja: ",givenmoney)
                    return False

                diff = cost-givenmoney
                print("Amount Due: ",diff)
                m = int(input())
                givenmoney += m
                i+=1
        if givenmoney >= cost:
            if givenmoney == cost:
                self.__money += cost
                return True
            elif givenmoney > cost:
                diff = givenmoney - cost
                print("\nHere's Your Change: ",diff)
                self.__money += cost
                return True
        

    def ordermoney(self,order,money):
        if order == "espresso": 
            return self.takemoney(money,200)
        if order == "cappuccino":
            return self.takemoney(money,300)
        if order == "latte":
            return self.takemoney(money,150)


class CoffeeMachine(Money):
    def __init__(self,water,milk,coffee):
        super().__init__()
        self.__water = water
        self.__milk = milk
        self.__coffee = coffee
        self.__sale = 0

    @staticmethod
    def prep_order(order,coffee,milk,water,money):
        row = {"order":order,"coffee left":coffee,"milk left":milk,"water left":water,"Money":money}
        data = json.dumps(row)
        Path("coffee.json").write_text(data)
        print("Preparing Your",order.capitalize())  
        time.sleep(2)
        print("Here's Your",order.title()) 



    def refil(self):
        c = input("Default of Custom Refil: ")
        if c.lower() == "default":
            self.__water += 500
            self.__milk += 500
            self.__coffee += 500
            print("Refil Successfull!")
        elif c.lower() == "custom":
            self.__water += int(input("Water: "))
            self.__milk += int(input("Milk: "))
            self.__coffee += int(input("Coffee: "))
            print("Refil Successfull!")
        else:
            print("Pardon?")    
            

    def report(self):
        if self.__water < 0 and self.__milk < 0 and self.__coffee < 0:
            self.__water = 0
            self.__milk = 0
            self.__coffee = 0  

        return self.__water,self.__milk,self.__coffee,self.passmoney(),self.__sale

    def dispense(self,order):
        if order.lower() == "espresso" and self.__water > 100 and self.__milk > 200 and self.__coffee > 50 :
            cost = int(input("Please pay Rs.200: "))
            self.ordermoney(order,cost)  
            self.__sale += 1
            self.__coffee -= 50
            self.__water -= 100
            self.__milk -= 200 
            self.prep_order(order,self.__coffee,self.__milk,self.__water,self.passmoney())

        if order.lower() == "cappuccino" and self.__water > 50 and self.__milk > 250 and self.__coffee > 80:
            cost = int(input("Please pay Rs.300: "))
            self.ordermoney(order,cost)
            self.__coffee -= 50
            self.__water -= 100
            self.__milk -= 200 
            self.__sale += 1
            self.prep_order(order,self.__coffee,self.__milk,self.__water,self.passmoney())

        if order.lower() == "latte" and self.__water > 150 and self.__milk > 150 and self.__coffee > 30:
            cost = int(input("Please pay Rs.150: "))
            self.ordermoney(order,cost)
            self.__coffee -= 50
            self.__water -= 100
            self.__milk -= 200 
            self.__sale += 1
            self.prep_order(order,self.__coffee,self.__milk,self.__water,self.passmoney())

        elif self.__water < 50 and self.__milk < 150 and self.__coffee < 30:
            print("Sorry Resources to prepare",order.title(),"has depleted..\nNeeds Refil")



