enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope
def drink_potion():
    potion_strength = 2 # This variable is defined inside a function. Hence, it cannot be accessed outside.
    print(potion_strength)

drink_potion()
print(potion_stength)

# Global scope
player_health = 10 # This variable is defined outside the function and it can be accessible any where.
def drink_potion():
    potion_strength = 2 # This variable is defined inside a function. Hence, it cannot be accessed outside.
    print(player_health)

drink_potion()
print(player_health)

# Similarly it's applicable on the function as well if its inside the function or outside the function
def game():
    def health()
        print(player_health)
print(health()) # This will cause error because function health is defined inside a function and is not in global scope