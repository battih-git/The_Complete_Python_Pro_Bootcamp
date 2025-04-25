import pandas as pd
df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data = pd.DataFrame(df['Primary Fur Color'].value_counts())
data.to_csv('squirrel_count.csv')