
import os
import pandas as pd
path1= "C:/OO"
path2="C:/AAndroid"
path3='C:/co-occurences'
for elem in os.listdir(path1):
    for elm in os.listdir(path2):
        if elem==elm:
            a = pd.read_csv(path1 +'/'+elem)
            b = pd.read_csv(path2 +'/'+elm)
            merged = a.merge(b,on='Class')
            merged.to_csv(path3 +'/'+elem, index=False)
            
