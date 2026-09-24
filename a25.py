import pandas as pd
import numpy as np
a = pd.Series([10,20,30,40], index = ['delhi','mumbai','kolkata','chennai'])
b = pd.Series([189,208,149,157], index = ['delhi','mumbai','kolkata','chennai'])
c = pd.Series([7916,8508,7226,7617], index = ['delhi','mumbai','kolkata','chennai'])
d = pd.DataFrame({'pop':a,'hos':b,'sch':c})
print(d)
print(d.loc['chennai':'chennai','pop':'pop'])
print(d.iloc[3:4:,0:1])
d.rename({'pop':'po'}, axis = 1, inplace = True)
print(d)
print(d.at['chennai','po'])
print(d.iat[3,0])
d.loc['delhi']= [8,2,3]
print(d)
d.loc[:,'po']=0 
print(d)
d.po['delhi'] = 4
print(d)
d.rename(index = {'delhi':'del'},columns = {'sch':'scool'}, inplace = True)
print(d)
