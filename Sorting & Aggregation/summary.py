import pandas as pd

data = {
    "Name" : ["Vaibhav","Kalpit","Arun"],
    "Age" : [24,35,20],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)

print(df["Salary"].mean())
print(df["Salary"].sum())
print(df["Salary"].max())
print(df["Salary"].min())