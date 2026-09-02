import pandas as pd

data = {
    "Name" : ['Vaibhav','Kalpit','Ram','Shayam','Kamlesh','Anaya','Rahul','Sameer'],
    "Age" : [24,26,25,35,31,29,40,22],
    "Salary" : [40000,45000,50000,70000,52000,48000,61000,57000],
    "Performance score" : [85,90,88,91,94,98,75,83]
}

df = pd.DataFrame(data)
print(df)

# Methos 1 
df["Bonus"] = df["Salary"] * 0.1
print(df)

# Insert method -> Best method used to ass column at any index
# insert(index,"column name",value)

df.insert(0,"Employee ID", [10,20,30,40,50,60,70,80])
print(df)