# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: 'Python 3.8.0 64-bit (''anly560-pyEnv'': venv)'
#     name: python38064bitanly560pyenvvenv177919d4f22f496dbe1b96ea20e55ec3
# ---

# # Pandas Puzzles (solution)
# ### Inspiration from [ajcr/100-pandas-puzzles] (https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles.ipynb)
# ---

# 1. Import pandas under the alias pd

import pandas as pd 

# ## Dataframe basics
# #### Selecting, Sorting, adding and aggregating data in dataframes...
#
# Consider the following Python dictionary data and Python list labels:

# +
import numpy as np 

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# -

# 2. Create a DataFrame df from this dictionary data which has the index labels

df = pd.DataFrame(data, index=labels)

# 3. Display a summary of the basic information about this DataFrame and its data (hint: there is a single method that can be called on the DataFrame).

df.dtypes         # data types
df.index          # index
df.describe()     # short summary

# 4. Return the first 3 rows of the DataFrame df.

df.head(3)

# 5. Select just the 'animal' and 'age' columns from the DataFrame df.

df.iloc[:, 0:2]

# 6. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].

df.iloc[[3, 4, 8], 0:2]

# 7. Select only the rows where the number of visits is greater than 3.

df[df['visits'] > 2]

# 8. Select the rows where the age is missing, i.e. it is NaN.

df[pd.isna(df['age'])]

# 9. Select the rows where the animal is a cat and the age is less than 3.

df[(df['animal'] == 'cat') & (df['age'] < 3)]

# 10. Select the rows the age is between 2 and 4 (inclusive).

df[(df['age'] >= 2) | (df['age'] <= 4)]

# 11. Change the age in row 'f' to 1.5.

df.loc['f','age'] = 1.5     # update value
df.loc['f', 'age']          # print

# 12. Calculate the sum of all visits in df (i.e. find the total number of visits).

df.loc[:, 'visits'].sum()

# 13. Calculate the mean age for each different animal in df.

df.loc[:, ['animal', 'age']].groupby('animal').mean()

# 14. Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.

df.loc['k'] = ['wolf', 5, 4, 'yes']             # appending row to existing df
df = df.drop('k')                               # deleting row 'k' from existing df
df                                              # show df

# 15. Count the number of each type of animal in df.

df.loc[:,['animal']].groupby('animal').size()

# 16. Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order (so row i should be first, and row d should be last).

df.loc[:, ['animal', 'age', 'visits']].sort_values(["age", "visits"], ascending = [False, True])

# 17. The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False.

df['priority'] = df['priority'].map({'yes': True, 'no': False})
df['priority']

# 18. In the 'animal' column, change the 'snake' entries to 'python'.

df.loc[df['animal'] == 'snake', 'animal'] = 'python'            # replace 'snake' to 'python'
df.loc[:, 'animal']                                             # display 'animal' col.

# 19. For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column is a number of visits and the values are the mean ages (hint: use a pivot table).

df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')

# # Series and DatetimeIndex
# ## creating and manipulating series with datetime...

# 20. Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers. Let's call this Series s.

dt = pd.date_range(start='01/01/2015', end='12/31/2015', freq='B')
s = pd.Series(data=np.random.rand(len(dt)), index=dt)
s

# 21. Find the sum of the values in s for every Wednesday.

s[s.index.weekday == 2].sum()

# 22. For each calendar month in s, find the mean of values.

s.groupby(s.index.month).mean()

# 23. For each group of four consecutive calendar months in s, find the date on which the highest value occurred.

s.groupby(pd.Grouper(freq='4M')).idxmax()           # use max() for value, idxmax() for index

# 24. Create a DateTimeIndex consisting of the third Thursday in each month for the years 2015 and 2016.

pd.date_range(start='01/01/2015', end='12/31/2016', freq='WOM-3THU')

# # Cleaning Data
# #### Consider following data....

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})
df

# 25. Some values in the the FlightNumber column are missing (they are NaN). These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Modify df to fill in these missing numbers and make the column an integer column (instead of a float column).

df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df

# 26. The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new temporary DataFrame called 'temp' with the correct values. Assign the correct column names 'From' and 'To' to this temporary DataFrame.

temp_df = df.From_To.str.split('_', expand=True)            # store the split in a temp. dataframe
temp_df.columns = ['From', 'To']                            # Name the columns
temp_df

# 27. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame 'temp'. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

temp_df['From'] = temp_df['From'].str.capitalize()
temp_df['To'] = temp_df['To'].str.capitalize()
temp_df

# 28. Delete the From_To column from 41. Delete the From_To column from df and attach the temporary DataFrame 'temp' from the previous questions.df and attach the temporary DataFrame from the previous questions.

df = df.drop('From_To', axis=1)                 # drop 'From_To' col from original dataframe
df = df.join(temp_df)                           # append the temporary dataframe with the original dataframe
df

# 29. In the Airline column, you can see some extra puctuation and symbols have appeared around the airline names. Pull out just the airline name. E.g. '(British Airways. )' should become 'British Airways'.

# using regex ([a-zA-Z\s]+) extract just the name containing letters where single space is allowed and then use strip() method to get rid of any leading or trailing spaces...
df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
df

# 30. In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN.
# Expand the Series of lists into a new DataFrame named 'delays', rename the columns 'delay_1', 'delay_2', etc. and replace the unwanted RecentDelays column in df with 'delays'.

delay_df = df['RecentDelays'].apply(pd.Series)                                              # using apply() convert list into Series...
delay_df.columns = [f'delay_{n}' for n in range(1, len(delay_df.columns)+1)]                # using list comprehensions name the columns of temporary delay dataframe
df = df.drop('RecentDelays', axis=1)                                                        # drop the original recent delays column
df = df.join(delay_df)                                                                      # join the temporary delay dataframe to original dataframe
df
