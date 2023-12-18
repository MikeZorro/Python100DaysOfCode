from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
paymentModule = MoneyMachine()

decision = input("What would you like? espresso/latte/cappuccino:")
while decision != "exit":
    if decision == "report":
        coffeeMaker.report()

    elif decision == "espresso" or "latte" or "cappuccino":
        drinkName = decision
        if coffeeMaker.is_resource_sufficient(menu.find_drink(drinkName)):
            paymentModule.make_payment(menu.find_drink(drinkName).cost)
            coffeeMaker.make_coffee(menu.find_drink(drinkName))
    decision = input("What would you like? espresso/latte/cappuccino:")

paymentModule.report()
print("Thank you for using our machine!")
