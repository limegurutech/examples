# import pandas as pd
# df = pd.read_csv("weather-data/2006-04-10.csv", parse_dates=["Formatted Date"])
# mean = df['Temperature (C)'].mean()
# print(mean)


import dask.dataframe as dd
df = dd.read_csv("weather-data/2006-*-*.csv", 
parse_dates=["Formatted Date"])
print(df.head())
all_day_mean = df['Temperature (C)'].mean().compute()
print('Temp all_days_mean:' + str(all_day_mean))

df['date'] = df['Formatted Date'].dt.date

daily_mean = df.groupby("date")['Temperature (C)'].mean().compute()
print("Temp daily_mean: "+ str(daily_mean))

