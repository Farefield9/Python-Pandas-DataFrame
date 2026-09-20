import pandas as pd
import numpy as np
symbol = pd.Series(['h','he','li','be'],['hydrogen','helium','lithium','berilium'])
print(symbol)
atomicno = pd.Series([1,2,3,4],['hydrogen','helium','lithium','berilium'])
print(atomicno)
a = pd.DataFrame({'s':symbol,'at':atomicno} )
print(a)
a = pd.Series([1,2,3],['a','b','c'])
b = pd.Series([4,5,6],['a','b','c'])
print(a)
c = pd.DataFrame([a,b])
print(c)
