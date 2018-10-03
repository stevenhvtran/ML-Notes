import pandas as pd

# Read CSV data
min_temp = pd.read_csv('data/daily_min_temp_melbourne.csv')
max_temp = pd.read_csv('data/daily_max_temp_melbourne.csv')
solar_exp = pd.read_csv('data/daily_solar_exposure_melbourne.csv')

# Get only wanted columns
max_temp = max_temp[['Year', 'Month', 'Day', 'Maximum temperature (Degree C)']]
min_temp = min_temp[['Year', 'Month', 'Day', 'Minimum temperature (Degree C)']]
solar_exp = solar_exp[['Year', 'Month', 'Day', 'Daily global solar exposure (MJ/m*m)']]

# Rename columns
min_temp.columns = ['year', 'month', 'day', 'min_temp']
max_temp.columns = ['year', 'month', 'day', 'max_temp']
solar_exp.columns = ['year', 'month', 'day', 'solar_exp']

# Merge dataframes on dates
dates = ['year', 'month', 'day']
min_max_temp = pd.merge(min_temp, max_temp, how='left', left_on=dates, right_on=dates)
df = pd.merge(min_max_temp, solar_exp, how='left', left_on=dates, right_on=dates)

# Drop rows with null data
df = df.dropna()
df = df.reset_index()
df = df.drop('index', axis=1)

df.to_csv('./data/bom_data.csv')
