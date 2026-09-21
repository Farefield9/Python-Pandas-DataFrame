import pandas as pd
import numpy as np
a = pd.DataFrame([['cold','virus'],['chickepox','virus'],['cholera','bacteria'],['tb','bacteria']], columns = ['diseasename','agent'])
print(a)
print(a[['diseasename','agent']][a['agent']=='virus'])
print(a[a['diseasename']=='cold'])
a.drop(2, axis = 0, inplace = True)
print(a)
a.loc[4]=['covid19','virus']
print(a)
print(a.tail(2))
a['recover days']= [5,15,2,100]
print(a)
a.drop('agent',axis = 1, inplace = True)
print(a)
a.insert(1,'treatment','medicine')
print(a)
