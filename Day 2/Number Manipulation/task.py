bmi = 84 / 1.65 ** 2
print(bmi) # Original value is float
print(int(bmi)) # Flooring the number removes the decimal with the help of type casting

print(round(bmi)) # It converts to int round up/down based on decimal is <> 0.5

print(round(bmi,2)) # If we want limited n digits in float we can use the round function

score = 0
# Assignment operator

score += 1
print(score)
score *= 2
print(score)
score -= 1
print(score)
score /= 1
print(score)


# f-strings
# print("Your score is " + score) This will result into type error because of multiple data types. f-string can be useful over here
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, Your height is {height}, Your winning is {is_winning}")