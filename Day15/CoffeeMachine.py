MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resources():
    """Prints remaining resources"""
    print(resources.get("water"), "ml")
    print(resources.get("milk"), "ml")
    print(resources.get("coffee"), "g")


def pay(coffee_type):
    """Processes the payment of given coffee type espresso/latte/cappuccino"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    cash = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if cash >= MENU[coffee_type]["cost"]:
        change = cash - MENU[coffee_type]["cost"]
        print("Your change is: ","{:.2f}".format(change))
        return True
    else:
        print("Not enough money!")
        print("Returning your change.")
        return False


def order_coffee(coffee_type):
    """Orders coffee"""
    coffee = MENU.get(coffee_type)
    if resources["water"] < coffee["ingredients"]["water"]:
        print("Not enough water!")
    elif resources["milk"] < coffee["ingredients"]["milk"]:
        print("Not enough milk!")
    elif resources["coffee"] < coffee["ingredients"]["coffee"]:
        print("Not enough coffee!")
    else:
        if pay(coffee_type):
            resources["water"] = resources["water"] - int(coffee["ingredients"]["water"])
            resources["milk"] = resources["milk"] - int(coffee["ingredients"]["milk"])
            resources["coffee"] = resources["coffee"] - int(coffee["ingredients"]["coffee"])
            print("Enjoy your ", coffee_type)
        else:
            print("Payment not successful")


def add_resource(name, amount):
    resources[name] = resources[name] + amount


decision = input("What would you like? espresso/latte/cappuccino:")
while decision != "exit":
    if decision == "report":
        print_resources()
    elif decision == "add":
        what = input("What would you like to add? water/milk/coffee:")
        howMuch = int(input("How much?"))
        add_resource(what, howMuch)
    elif decision == "espresso" or "latte" or "cappuccino":
        order_coffee(decision)
    decision = input("What would you like? espresso/latte/cappuccino:")
print("Thank you for using our machine!")
