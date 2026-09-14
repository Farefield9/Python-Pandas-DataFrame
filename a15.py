import pandas as pd
import numpy as np
a = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index = [10,20,30], columns = ['a','b','c'])
print(a)
a.loc[40] = [10,11,12]
print(a)
