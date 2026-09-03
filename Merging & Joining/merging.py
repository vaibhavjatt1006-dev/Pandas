import pandas as pd

df_customers = pd.DataFrame({
    "CustomerID" : [1,2,3],
    "Name" : ["Vaibhav","Kalpit","Suresh"]
})

df_orders = pd.DataFrame({
    "CustomerID" : [1,2,4],
    "Price" : [250,450,100]
})

print(pd.merge(df_customers,df_orders, on="CustomerID",how="inner"))
print(pd.merge(df_customers,df_orders, on="CustomerID",how="outer"))
print(pd.merge(df_customers,df_orders, on="CustomerID",how="left"))
print(pd.merge(df_customers,df_orders, on="CustomerID",how="right"))
