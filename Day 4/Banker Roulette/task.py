import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Method
print(random.choice(friends))

# 2nd Method
index = random.randint(0,4)
print(friends[index])