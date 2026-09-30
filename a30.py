import pandas as pd
import numpy as np
a = [[1,2,3],[4,5,6],[7,8,9]]
c = pd.DataFrame(a,index = ['a','b','c'],columns = ['x','y','z'])
print(c.loc['a',])
