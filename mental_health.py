import pandas as pd
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