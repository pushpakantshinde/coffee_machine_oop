from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True

while should_continue:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = menu.find_drink(choice)
        should_continue = coffee_maker.is_resource_sufficient(drink)
        if should_continue:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        should_continue = False