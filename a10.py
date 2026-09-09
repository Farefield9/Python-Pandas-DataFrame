import pandas as pd
import numpy as np
a = {'arnab':pd.Series([1,2]),
     'ramit':pd.Series([3,4]),
     'samridhi':pd.Series([5,6])}
b = pd.DataFrame(a)
print(b)
