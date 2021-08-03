from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_service_finished = False

    while not is_service_finished:
        choice = input(f"What would you like? ({menu.get_items()}): ")
        if menu.find_drink(choice) is not None:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            print("Machine is shutting down..")
            is_service_finished = True
        else:
            print("Invalid command! Try again.")
