import pandas as pd

data = {
    "Name" : ["Vaibhav","Kalpit","Arun"],
    "Age" : [24,35,20],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=False, inplace=True)
print(df)