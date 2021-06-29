"""
    DAY 15: Coffee Machine
"""

from typing import Dict

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
}


def _print_report(current_resources: Dict) -> None:
    """
        Function which prints report with info about current resources availability.
    """
    for name, amount in current_resources.items():
        if name == "coffee":
            unit = "g"
        elif name in ("water", "milk"):
            unit = "ml"
        else:
            unit = "$"
        print(f"{name}: {amount}{unit}")


def _check_resources(coffee_type: str) -> bool:
    """
        Function which check if there are enough resources for preparing a coffee.
    """
    for name, amount in resources.items():
        if name in MENU[coffee_type]["ingredients"].keys():
            if amount < MENU[coffee_type]["ingredients"][name]:
                print(f"Not enough {name} to prepare a {coffee_type}.")
                return False
    return True


def _process_coins(coffee_type: str, current_resources: Dict) -> bool:
    """
        Function for processing coins in coffee machine.
    """
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    print(f"You inserted {total_money}$")
    coffee_cost = MENU[coffee_type]["cost"]
    if total_money >= coffee_cost:
        change = total_money - coffee_cost
        print(f"Here is your change {round(change, 2)}$")
        if "money" not in current_resources:
            current_resources["money"] = 0
        current_resources["money"] += coffee_cost
        return True
    else:
        print(f"Not enough money to make a {coffee_type}. Returning your money.. -> {total_money}$")
        return False


def _prepare_coffee(coffee_type: str, current_resources: Dict) -> None:
    """
        Function which prepares coffees and decrease resources.
    """
    if _check_resources(coffee_type):
        if _process_coins(coffee_type, current_resources):
            for ingredient, amount in MENU[coffee_type]["ingredients"].items():
                resources[ingredient] = resources[ingredient] - amount
            print(f"Here is your {coffee_type} ☕. Enjoy!")


def coffee_machine() -> None:
    """
        Main function of coffee machine program.
    """
    is_work_finished = False
    print("Good morning. I'm coffee machine")

    while not is_work_finished:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        if choice in MENU.keys():
            _prepare_coffee(choice, resources)
        elif choice == "report":
            _print_report(resources)
        elif choice == "off":
            is_work_finished = True
        else:
            print("Wrong command. Try again!")


if __name__ == "__main__":
    coffee_machine()
