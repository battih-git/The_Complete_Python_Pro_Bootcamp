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

# TODO 1 Create a prompt to take user input for coffee
def user_input():
    print("Welcome to Coffee vending Machine.")
    coffee_type = input("What would you like (espresso/latte/cappuccino) :")
    return coffee_type


# TODO 2 Turn off coffee machine by entering off to the prompt
# TODO 3 Create print report
def print_resources(resource):
    for key,value in resource.items():
        if key == 'water' or key == 'milk':
            print(f"{key} : {value}ml")
        if key == 'coffee':
            print(f"{key} : {value}g")
        if key == 'money':
            print(f"{key} : ${value}")


# TODO 4 Check resource if it's sufficient for users order
def check_resources(user_choice, resource):
    for key,value in user_choice.items():
        if user_choice[key] > resource[key]:
            print(f"Sorry there is not enough {resource[key]}")
            return False
        else:
            return True


# TODO 5 Process Coins
def process_coins(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (nickles * 0.05) + (dimes * 0.10) + (pennies * 0.01)
    return total

# TODO 6 Check transaction successfully
def transaction_status(total, coffee_type):
    if total < MENU[coffee_type]['cost']:
        return True
    return False

# TODO 7 Make coffee

coffee = user_input()
user_preference = MENU[coffee]['ingredients']
print(user_preference)
enough_resources = check_resources(user_preference,resources)
print(enough_resources)
if enough_resources:
    inserted_money = process_coins(co)
    transaction_successful = transaction_status(pro)

