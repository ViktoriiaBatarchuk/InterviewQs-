'''
Number: 149
Here is the task for today:
Suppose you're given the table, showing open and close prices as well as trading volume for a particular equity.
In Python, write code to show the volume weighted average price (VWAP) for a rolling 2-day window.
The VWAP is calculated as [(Price * Volume) / Volume].
In this case, your resultant table would start on 1/3/2019 and roll daily from there.
'''

import pandas as pd

#Create dataframe with the datasets of open and close prices as well as trading volume for a particular equity
data = {
    'Date': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05',
             '2019-01-06', '2019-01-07', '2019-01-08', '2019-01-09', '2019-01-10',
             '2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14', '2019-01-15'],
    'Close': [0.214420, 0.338620, 1.051536, 0.911552, 0.997130,
              0.426184, 0.376917, 0.543065, 1.678835, 0.481132,
              0.091329, 0.308104, 0.698701, 0.878822, 1.159343],
    'Open': [1.808281, 0.254375, 1.151315, 0.455321, 0.359723,
             0.987991, 0.307812, 0.136257, 0.836795, 0.790461,
             0.910299, 0.843959, 0.947239, 1.046117, 0.427352],
    'Volume': [759, 1324, 1787, 2908, 713, 2330, 2592, 1265, 2674,
               2508, 806, 647, 2351, 2840, 2302]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date']) #converts the values in the 'Date' column of the DataFrame df
                                        # to pandas datetime objects
df.set_index('Date', inplace=True)  #set_index function used to set a specific column as the index of the DataFrame
                                    #inplace=True: This argument means the operation will modify df directly rather
                                    #than creating a new DataFrame

#Calculate VWAP for a rolling 2-day window on Close prices
df['VWAP_2d'] = (df['Close']*df['Volume']).rolling(window=2).sum()/df['Volume'].rolling(window=2).sum()
#With window=2, the .rolling(window=2).sum() will compute the sum of every two consecutive rows
# in the DataFrame column it's applied to, shifting forward by one row for each calculation
#There will be some NaN values. Therefore we need to drop them
#Drop NaN values generated from the first row to get rolling results
result = df[['Close','Open','Volume','VWAP_2d']].dropna()
result = df[['Close', 'Open', 'Volume', 'VWAP_2d']].iloc[2:] #skip two rows


print(result)