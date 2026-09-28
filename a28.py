import pandas as pd
import numpy as np
a = pd.DataFrame([[1,2],[3,4]], columns = ['x','z'], index = ['o','m'])
print(a)
a['y'] = [20,30]
print(a)
a.loc['g']= [10,20,30]
print(a)
