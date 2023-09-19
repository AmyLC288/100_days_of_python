MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "money": 0,
}

def sufficient_resources(ingredients_needed):
    for item in ingredients_needed:
        if ingredients_needed[item] > resources[item]:
            print(f"Sorry, there is not enough {item} for this selection. ")
            return False
        else:
            return True

def make_coffee(SELECTION, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
        print(f"Here is your {SELECTION}. Enjoy!")
        return


def calulate_change (QUARTERS, DIMES, NICKELS, PENNIES):
    """function to calculate the change needed to be returned"""
    total = 0.00
    total += (QUARTERS * 0.25)
    total += (DIMES * 0.10)
    total += (NICKELS * 0.05)
    total += (PENNIES * 0.01)
    total = round(total, 2)
    change = total - MENU[SELECTION]["cost"]
    if total > MENU[SELECTION]["cost"]:
        return round(change,2)
    else:
        change = total
        return "You do not have enough money. Here is a refund."


machine_on = True

while machine_on == True:
    SELECTION = input("What would you like? (espresso/latte/cappuccino):").lower()
    if SELECTION == "off":
        machine_on = False
    elif SELECTION == "report":
     print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g")
     print(f"Money: {resources['money']}")
    else:
        DRINK_SELECTION = MENU[SELECTION]
        drink_ingredients = MENU[SELECTION]["ingredients"]
        if sufficient_resources(DRINK_SELECTION["ingredients"]):
            print("Please insert coins.")
            QUARTERS = int(input("How many quarters? "))
            DIMES = int(input("How many dimes? "))
            NICKELS = int(input("How many nickles? "))
            PENNIES = int(input("How many pennies? "))
            print(calulate_change(QUARTERS, DIMES, NICKELS, PENNIES))
            make_coffee(SELECTION, drink_ingredients)
            