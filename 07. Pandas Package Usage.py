import pandas as pd
import matplotlib.pyplot as py

# Some basics

# Creating dataframe and series

fruit_sales = pd.DataFrame({'Apples': [39,27], 'Orange': [71,43]}, index = ['2019 Sales', '2020 Sales'])

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')

# Reading files
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col = 0) # index_col syntax, it will remove default index columns

df = pd.read_csv('/Roy/Python/pokemon.csv')
# print(df.head(3)))

# df_xlsx = pd.read_excel('/Roy/Python/pokemon.xlsx')
# df_txt = pd.read_csv('/Roy/Python/Notepad.txt', delimiter=',')
# print(df_txt)

# print(df.columns) # Reading headers

# Reading columns
# iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
# So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

# print(df['Name'][0:5]) # Reading one column with 5 rows or
# print(df.Name)
# print(df.iloc[0,1]) # the first value or
# print(df.Name.iloc[0])
# print(df[['Name', 'Type 1', 'HP', 'Attack']])  # to read list of column names

# Using iloc to fetch data (left side of , is for row and right side is for column indexes
# print(df.iloc[1:3, 1:4])
# print(df.iloc[2, 2])

# Read each row
# print(df.iloc[0:5])
# print(df.iloc[0, :])  # Select the first row of data (the first record) 
# for index, row in df.iterrows():  # all info of each row organized in a column
#     print(index, row)

# Looking for particular info on each row of a column
# print(df.loc[df['Type 1'] == 'Fire'])

# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews
indices = [1, 2, 3, 5, 8]
sample_reviews = df.loc[indices, :]  # either loc or iloc is fine

indices = [0, 1, 10, 100]
cols = ['country', 'province', 'region_1', 'region_2'] # similar way to select particular columns
df = reviews.loc[indices, cols]

# Create a DataFrame italian_wines containing reviews of wines made in Italy
italian_wines = reviews.loc[(reviews['country']=='Italy')]  #or
italian_wines = reviews[reviews.country == 'Italy']

# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
top_oceania_wines = reviews.loc[((reviews['country']=='Australia') | (reviews['country']=='New Zealand')) 
                                & (reviews['points'] >= 95)]  # or
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]

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

# Filtering data
# isin is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select wines only from Italy or France:
filter0 = df.loc[(df.Type 1.isin(['Grass', 'Fire'])]
filter1 = df.loc[(df['Type 1'] == 'Grass')]
filter2 = df.loc[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')]
filter3 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 80)]
                  
# isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN).
df.loc[(df.Type 1.notnull()]

print(filter1)
print(filter2.head(5))
print(filter3)
# py.bar(df["Generation"], df["Generation"].count, width=0.8, bottom=None, align='center', data= df)
        
# Assigning data to a DataFrame
df['critic'] = 'everyone'
df['index_backwards'] = range(len(df), 0, -1) # 0 means from first to -1 meaning last
