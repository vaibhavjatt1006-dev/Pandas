import pandas as pd

data = {
    "Name" : ['Vaibhav','Kalpit','Ram','Shayam','Kamlesh','Anaya','Rahul','Sameer'],
    "Age" : [24,26,25,35,31,29,40,22],
    "Salary" : [40000,45000,50000,70000,52000,48000,61000,57000],
    "Performance score" : [85,90,88,91,94,98,75,83]
}

df = pd.DataFrame(data)
print(df)

# single condition
high_salary = df[df["Salary"] > 50000]
print(high_salary)

# Multiple conditions (and)
age_salary = df[(df["Age"] > 30) & (df["Salary"] > 50000)]
print(age_salary)

# Multiple conditions (or)
age_salary = df[(df["Age"] > 30) | (df["Performance score"] > 90)]
print(age_salary)