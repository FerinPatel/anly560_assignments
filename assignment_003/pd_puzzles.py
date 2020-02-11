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

# # Pandas Puzzles
# ### Inspired by [ajcr/100-pandas-puzzles] (https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles.ipynb)
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


