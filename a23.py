import pandas as pd
import numpy as np
a = pd.DataFrame({'rollno':[1,2,3,4,5], 'name':['aditya','bakwhwat','chirag','deepak','eva'], 'english':[23,18,27,11,17],'hindi':[20,1,23,3,21], 'maths':[28,25,30,7,24]})
print(a)
print(a.loc[1:3,['english']])
print(a[a['name']=='eva']['hindi'])
print(a.values)
print(a.loc[1:2,:])
a['maths']+=4
print(a)
print(a[a['maths']<20].loc[:,'rollno':'name'])
print(a.loc[:,'english':'maths'].sum(1))
