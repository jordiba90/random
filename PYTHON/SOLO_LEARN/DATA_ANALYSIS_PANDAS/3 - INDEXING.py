#DATA_ANALYSIS_PANDAS_INDEXING

#######################################################################################################################
#Rows with .loc
#######################################################################################################################

import pandas as pd

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
                                  
print("PRESIDENTS_LINCOLN :\n")
print(presidents_df.loc['Abraham Lincoln'])

print("\nPRESIDENTS_LINCOLN_TYPE :\n")
print(type(presidents_df.loc['Abraham Lincoln']))

print("\nPRESIDENTS_ROWS :",presidents_df.loc['Abraham Lincoln'].shape[0])

print("\nPRESIDENTS_SLICE_LINCOLN_TO_GRANT :\n")
print(presidents_df.loc['Abraham Lincoln':'Ulysses S. Grant'])

#######################################################################################################################
#Rows with .iloc
#######################################################################################################################

print("\nPRESIDENTS_SLICE_15:\n")
print(presidents_df.iloc[15])

print("\nPRESIDENTS_SLICE_15_TO_18 :\n")
print(presidents_df.iloc[15:18])

#######################################################################################################################
#Columns
#######################################################################################################################

print("\nPRESIDENTS_COLUMNS :\n")
print(presidents_df.columns)

#print(presidents_df['height'])
print("\nPRESIDENTS_HEIGHT :",presidents_df['height'].shape[0])

print("\nPRESIDENTS_HEIGHT_AGE :\n")
print(presidents_df[['height','age']].head(n=3))

#######################################################################################################################
#More with .loc
#######################################################################################################################

print("\nPRESIDENTS_ORDER_HEIGHT_AGE :\n")
print(presidents_df.loc[:, 'order':'height'].head(n=3))
