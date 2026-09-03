import pandas as pd

data = {
    "Name" : ["Vaibhav","Kalpit","Arun","Tarun","Varun"],
    "Age" : [24,35,20,24,35],
    "Salary" : [70000,80000,40000,55000,61000]
}

df = pd.DataFrame(data)

grouping = df.groupby(["Age","Name"])["Salary"].sum()
print(grouping)