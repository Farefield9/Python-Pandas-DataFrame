import pandas as pd
import numpy as np
a = pd.DataFrame([[1,2,3],[5,6,8]], columns = ['a','b','c'])
print(a.iloc[::-1,:])
a['c'] = [4,9]
print(a)
a.rename(index = {0:'zero',1:'one'}, inplace = True)
print(a)
a.loc[len(a.index)] = [5,7,9]
print(a)
print(a['b']>2)
print(min(a))
a.insert(0,'z',[0,00,000])
print(a)
a.drop('z', axis = 1, inplace = True)
print(a)
