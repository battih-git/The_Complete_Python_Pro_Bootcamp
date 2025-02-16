game_level = 3
enemies = ['Skeleton', 'Zombie','Alien']

new_enemy = ''
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # Anything declared between the block of code apart from function can be used globally