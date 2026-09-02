import pandas as pd

data = {
    "Name" : ['Vaibhav','Kalpit','Ramesh'],
    "Age" : [10,20,30],
    "Place" : ['Mumbai','Delhi','Banglore']
}

df = pd.DataFrame(data)
print(df)

# Index = False is used to remive tthe index 0,1,2 from the output file

# df.to_csv("output.csv",index=False) 
# df.to_json("output.json",index=False) 
df.to_excel("output.xlsx",index=False) 