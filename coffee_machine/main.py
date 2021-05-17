MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18,}, "cost": 1.5,},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24,}, "cost": 2.5,},
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24,},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Penny 1c 0.01
# Nickel 5c 0.05
# Dime 10c 0.10
# quarter 25c 0.25
money = 0


def print_report():
    if user_input == "report":
        return (
            f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${money}\n"
        )


def check_resources(order):
    if order == "espresso":
        if (
            resources["water"] >= MENU[order]["ingredients"]["water"]
            and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]
            and resources["milk"] >= MENU[order]["ingredients"]["milk"]
        ):
            return True
        else:
            return False
    elif order == "latte" or order == "cappuccino":
        if (
            resources["water"] >= MENU[order]["ingredients"]["water"]
            and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]
        ):
            return True
        else:
            return False


# print(check_resources(order=user_input))

print("What would you like? (espresso/latte/cappuccino):")
user_input = input()

