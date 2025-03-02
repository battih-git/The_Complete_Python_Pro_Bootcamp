from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine = True
while machine:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}): ")
    if user_input == 'off':
        machine = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(user_input.lower())
        if coffee_maker.is_resource_sufficient(item) and  money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)



