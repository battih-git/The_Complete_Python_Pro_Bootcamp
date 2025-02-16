import  art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract (n1,n2):
    return  n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

dict_operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    condition = True
    while condition:
        for key in dict_operations:
            print(key)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        result = dict_operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        user_confirmation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if user_confirmation.lower() == 'y':
            condition = True
            num1 = result
        else:
            condition = False
            calculator()

calculator()


