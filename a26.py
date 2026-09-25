import pandas as pd
import numpy as np
a = pd.DataFrame([[1,4,3],[4,2,6]], columns = ['a','b','c'])
print(a)
print(a.min(axis = 1))
print(a.sort_values('b'))
