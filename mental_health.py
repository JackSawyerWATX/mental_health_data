import pandas as pd
import numpy as np

health_data = pd.read_csv("Mental_Health_Care_in_the_Last_4_Weeks.csv", header=0)

# Drop rows missing data in important columns
health_data.dropna(subset=['Indicator', 'Group', 'State', 'Value'], inplace=True)

# Filter for Washington
health_data = health_data[health_data['State'] == 'Washington']

# Show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Increase column width so text doesn't get cut off
pd.set_option('display.max_colwidth', None)

print(health_data)
print(health_data['Indicator'].unique())
print(health_data.head())
print(health_data.tail())
print(health_data.index)
print(health_data.columns)
print(health_data.dtypes)
print(health_data.describe())
print(health_data.info())
print(health_data.shape)
print(health_data.to_numpy())
print(health_data.T)
print(health_data.sort_values(by='Value'))
print(health_data.groupby('Group').mean())
print(health_data['Value'].value_counts())
print(health_data['Value'].head())
print(health_data['Value'].tail())
print(health_data[100:300])