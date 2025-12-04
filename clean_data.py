import pandas as pd

health_data = pd.read_csv("Mental_Health_Care_in_the_Last_4_Weeks.csv", header=0, sep=",")

health_data.dropna(subset=['Indicator', 'Group', 'State', 'Value'], inplace=True)

print(health_data.describe())

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print()
print(health_data)
