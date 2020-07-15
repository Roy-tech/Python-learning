import pandas as pd
import matplotlib.pyplot as py

# Reading files
df = pd.read_csv('/Roy/Python/pokemon.csv')
# print(df.head(3)))

# df_xlsx = pd.read_excel('/Roy/Python/pokemon.xlsx')
# df_txt = pd.read_csv('/Roy/Python/Notepad.txt', delimiter=',')
# print(df_txt)

# print(df.columns) # Reading headers

# Reading columns

# print(df['Name'][0:5]) # Reading one column with 5 rows or
# print(df.Name)
# print(df[['Name', 'Type 1', 'HP', 'Attack']])  # to read list of column names

# Using iloc to fetch data (left side of , is for row and right side is for column indexes
# print(df.iloc[1:3, 1:4])
# print(df.iloc[2, 2])

# Read each row
# print(df.iloc[0:5])
# for index, row in df.iterrows():  # all info of each row organized in a column
#     print(index, row)

# Looking for particular info on each row of a column
# print(df.loc[df['Type 1'] == 'Fire'])

# Sorting/ describing data
# print(df.describe())
#
# print(df.sort_values('Name', ascending=False))

# sort 1st one ascending and 2nd one descending 1 & 0 means True and False respectively
# print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))

# Making changes to the data
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df['Total'])  # or
#
# df = df.drop(columns=['Total'])
# df["Total"] = df.iloc[:, 4:10].sum(axis=1)  # axis = 1 means horizontally and 0 means vertically

# You can create list of columns like following

# cols = list(df.columns.values)
# df_short = df[cols[0:4] + [cols[-1]] + cols[4:12]]  # cols[-1] putting in [] to show as list as it is one column
# print(df_short.head(5))

# Saving data
# df_short.to_csv("/Roy/Python/modified.csv", index=False)  # index to remove extra row number
# df_short.to_excel("/Roy/Python/modified.xlsx", index=False)
# df_short.to_csv("/Roy/Python/modified.txt", index=False, sep='/t')

# Filtering dara
filter1 = df.loc[(df['Type 1'] == 'Grass')]
filter2 = df.loc[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')]
filter3 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 80)]

print(filter1)
print(filter2.head(5))
print(filter3)
# py.bar(df["Generation"], df["Generation"].count, width=0.8, bottom=None, align='center', data= df)
