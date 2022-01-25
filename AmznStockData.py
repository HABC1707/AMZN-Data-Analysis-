#Amazon Stock Data Analysis

import matplotlib.pyplot as plt

import pandas as pd

#Read File
amzn = pd.read_csv('HistoricalData_AMZN.csv')

#Removes $ symbol
amzn = amzn.replace({'\$':''}, regex = True)

# Renaming column names and converting the data types
df = amzn
df.columns = ['Date', 'Close', 'Volume', 'Open', 'High', 'Low']

# Converting data types
df = df.astype({"Close": float, "Volume": int, "Open": float, "High": float, "Low": float})

# Closing price more than 3000
mask_closeprice = df.Close > 3000
high_price = df.loc[mask_closeprice]

#Plot Graph
df.plot(x='Date', y='Close', title="AMZN Stock Price")
plt.show()

#Dataframe View
print(amzn.head())
print()
print(amzn.tail())
print()
print(amzn.describe())
print()
print(amzn.dtypes)
print()
print(df.dtypes)
print()
print(df.describe())
print()
print(df.describe(include = "float"))
print()
print(df.describe(include = "object"))
print()
print(df.describe(exclude = "int"))
print()
print(df.describe(percentiles = [0.1, 0.5, 0.9]))
print()
print(high_price.head())

import pandas_datareader as dr

dr.get_data_tiingo('GOOG', api_key=’32185614c1896b0a9527f898a5d50d45423cb09f’)
