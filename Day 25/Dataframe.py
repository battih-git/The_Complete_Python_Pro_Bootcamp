# import csv
# with open('weather_data - Sheet1.csv') as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != 'temp':
#             tempratures.append(row[1])
# print(tempratures)

import pandas as pd
from numpy.ma.extras import average

data = pd.read_csv('weather_data - Sheet1.csv')
print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].tolist()
print(temp_list)
average_temp = sum(temp_list)/len(temp_list)
print(average_temp)

print(data['temp'].mean())
print(data['temp'].max())

print(data['condition'])
print(data[data['day']=='Monday'])

print(data[data['temp'] == data['temp'].max()])

monday = data[data['day']=='Monday']
print(monday['condition'])
print((monday['temp']*9/5)+32)

# Create a data frame from scratch
data_dict = {
    'students' : ['Amy','James','Angela'],
    'scores' : [76,56,65]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv('new_data.csv')