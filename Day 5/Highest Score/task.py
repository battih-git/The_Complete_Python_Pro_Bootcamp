student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# Sum the total value of scores
sum = 0
for score in student_scores:
    sum += score
print(sum)

# Search for the max number
max_num = student_scores[0]
for score in student_scores:
    if max_num < score:
        max_num = score

print(max_num)