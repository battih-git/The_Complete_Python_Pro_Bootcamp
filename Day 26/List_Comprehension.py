# List comprehension
numbers = [1,2,3,4]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
#
# print(new_list)

new_list = [n + 1 for n in numbers]
print(new_list)

# Shortens the code

name = 'Huzefa'
new_list = [letter for letter in name]
print(new_list)

new_list = [num*2 for num in range(1,6)]
print(new_list)

# Conditional List Comprehension
names = ['Alex', 'Beth', 'Caroline','Dave','Eleanor','Freddie']
short_names = [name for name in names if len(name)< 5]
print(short_names)

long_names = [name.upper() for name in names if len(name)>5]
print(long_names)