# Modifying Global Scope

enemies = "Skeleton"


def increase_enemies():
    enemies = 'Zombie'
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def increase_enemies():
    global enemies # By changing the variable scope to global. It can make changes to global variable.
    enemies = 'Zombie'
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


