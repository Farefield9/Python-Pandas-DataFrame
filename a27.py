import pandas as pd
import numpy as np
a = pd.DataFrame([[1,2,3,np.NaN,5],[6,7,np.NaN,9,10],[np.NaN,12,13,np.NaN,15],[16,17,18,19,20]], columns = ['c1','c2','c3','c4','c5'],
                 index = ['r1','r2','r3','r4'])
print(a)
print(a.loc['r1','c1'])
print(a.isnull())
print(a.dropna())
print(a.dropna(axis = 1))
print(a.fillna({'c1':0,'r2':3}))
