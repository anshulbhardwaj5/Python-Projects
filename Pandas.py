import pandas as pd
import numpy as np 
import matplotlib as plt

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(4, index=list(range(4)),dtype='float'),
                    'D' : pd.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(['You','Can','do','that']),
                    'F' : ('foo','off','ofo','oof')
                   })
                  
print(df2)
print(df2.dtype)

d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
print(ser)

ser = pd.Series(pd.Categorical(['a', 'b', 'a']))
print(ser.array)
