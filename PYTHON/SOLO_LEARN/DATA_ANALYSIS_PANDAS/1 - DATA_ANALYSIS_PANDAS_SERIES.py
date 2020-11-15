#DATA_ANALYSIS_PANDAS_SERIES

#######################################################################################################################
#
#######################################################################################################################

import numpy as np
import pandas as pd

print("INDEX_PANDAS :\n")
print(pd.Series([1, 2, 3], index=['a', 'b', 'c']))

print("\nINDEX_PANDAS_ARRAY :\n")
print(pd.Series(np.array([1, 2, 3]), index=['a', 'b', 'c']))

print("\nINDEX_PANDAS_DICTIONARY :\n")
print(pd.Series({'a': 1, 'b': 2, 'c':3}))

series = pd.Series({'a': 1, 'b': 2, 'c':3})
print("\nINDEX_SELECT_A_ELEMENT :\n")
print(series['a'])
