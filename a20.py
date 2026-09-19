import pandas as pd
import numpy as np
a = pd.DataFrame({'name':{101:'sapna',102:'anmol',103:'rishul',104:'sameep'}, 'agg':{101:56,102:67,103:75,104:76}, 'age':{101:16,102:18,103:16,104:19}})
print(a)
print(a[a['name']=='sapna'])
a.rename({101:'p1',102:'p2',103:'p3',104:'p4'}, inplace = True)
print(a)
a.rename({'agg':'points'}, axis = 1,  inplace = True)
print(a)
