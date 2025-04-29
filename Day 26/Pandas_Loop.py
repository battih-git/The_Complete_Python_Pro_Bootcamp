import pandas
import pandas as pd

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

# Looping through pandas data frame
students_data_frame = pd.DataFrame(student_dict)
print(students_data_frame)

# Loop through same comprehension method
# for (key,value) in students_data_frame.items():
#     print(key)

for (index,row) in students_data_frame.iterrows():
    if row['student'] == 'Angela':
        row['status'] = 'pass'
    else:
        row['status'] = 'fail'

print(students_data_frame)
