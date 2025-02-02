import random
import my_module # Custom module created.
random_int = random.randint(1,10) # To generate random number between two integer
print(random_int)
print(my_module.my_favourite_number)

random_number_0_1 = random.random() # To generate random number between 0-1 and returns the float value
print(random_number_0_1)

random_float = random.uniform(1,10) # To generate random float value between two given integers.
print(random_float)

# Heads or Tails
random_num = random.randint(0,1)
if random_num == 0:
    print("Head")
else:
    print("Tail")