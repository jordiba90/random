#DATA_ANALYSIS_PANDAS_DATAFRAMES

#######################################################################################################################
#DataFrames
#######################################################################################################################

import pandas as pd

wine_dict = {'red_wine': [3, 6, 5],'white_wine':[5, 0, 10]}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
print("SALES :")
print(sales)

print("\nSALES_WHITE_WINE :")
print(sales['white_wine'])

#######################################################################################################################
#Inspect a DataFrame - Shape and Size
#######################################################################################################################

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
#print("\nPRESIDENTS :\n",presidents_df)
print("\nPRESIDENTS_ROWS_AND_COLUMNS :\n",presidents_df.shape)

print("\nPRESIDENTS_ROWS :\n",presidents_df.shape[0])
print("\nPRESIDENTS_COLUMNS :\n",presidents_df.shape[1])

print("\nPRESIDENTS_DATA :\n",presidents_df.size)

#######################################################################################################################
#Inspect a DataFrame - Head and Tail
#######################################################################################################################

print("\nPRESIDENTS_HEAD_3 :\n",presidents_df.head(n=3))
print("\nPRESIDENTS_TAIL_5 :\n",presidents_df.tail())

print("\n")

#######################################################################################################################
#Inspect a DataFrame - Info
#######################################################################################################################

print("PRESIDENTS_INFO :\n",presidents_df.info())
