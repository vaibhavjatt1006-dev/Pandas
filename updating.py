import pandas as pd

data = {
    "Name" : ['Vaibhav','Kalpit','Ram','Shayam','Kamlesh','Anaya','Rahul','Sameer'],
    "Age" : [24,26,25,35,31,29,40,22],
    "Salary" : [40000,45000,50000,70000,52000,48000,61000,57000],
    "Performance score" : [85,90,88,91,94,98,75,83]
}

df = pd.DataFrame(data)
print(df)

# Method 1 -> Only used to change a single value
df.loc[1,"Performance score"] = 100
print(df)

# Method 2 -> updating full column
df["Salary"] = df["Salary"] * 1.05
print(df)