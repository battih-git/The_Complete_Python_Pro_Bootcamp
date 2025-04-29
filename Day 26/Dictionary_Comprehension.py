# Dictionary comprehension
# Syntax: new_dict = {new_key:new_value for item in list}
# Syntax: new_dict = {new_key:new_value for (key,value) in dict.items}
# Syntax with Conditional: new_dict = {new_key:new_value for (key,value) in dict.items}
import random

names = ['Alex', 'Beth', 'Caroline','Dave','Eleanor','Freddie']
students_score = {student:random.randint(1,100) for student in names}
print(students_score)

sample_scores = {'Alex': 88, 'Beth': 27, 'Caroline': 19, 'Dave': 17, 'Eleanor': 51, 'Freddie': 72}
pass_students  = {student:score for (student,score) in sample_scores.items() if score>=60}
pass_status = {student:'pass' if score>=62 else 'fail'  for (student,score) in sample_scores.items()}
print(pass_students)
print(pass_status)