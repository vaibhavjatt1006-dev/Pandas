import pandas as pd

data = {
    "Name" : ["Vaibhav","Kalpit","Arun"],
    "Age" : [24,35,20],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)

df.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True)
print(df)