import pandas as pd

list =[1,2,3,4]
print(type(list))
series =  pd.Series(list)
print(type(series))

df_titanic=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df_titanic)
df_titanic.