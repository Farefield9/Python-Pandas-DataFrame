import pandas as pd
import numpy as np
a = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], ['q','w','e','r'],['A','B','C','D'])
print(a)
a.drop(['q'], inplace = True)
print(a)
a.drop(['A'], axis = 1, inplace = True)
print(a)
a.rename({'w':'W'}, inplace = True)
print(a)
a.rename({'B':'b'}, axis = 1, inplace = True)
print(a)
a.loc[[True,False,True]]
print(a)
