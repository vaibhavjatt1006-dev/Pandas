import pandas as pd

df_Region1 = pd.DataFrame({
    "CustomerID" : [1,2],
    "Name" : ["Vaibhav","Kalpit"]
})

df_Region2 = pd.DataFrame({
    "CustomerID" : [3,4],
    "Name" : ["Ram","Shayam"]
})

print(pd.concat([df_Region1,df_Region2],axis=0, ignore_index=True))