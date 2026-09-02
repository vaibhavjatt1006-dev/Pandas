import pandas as pd

# df = pd.read_json("sample_Data.json")

data = {
    "Name" : ['Vaibhav','Kalpit','Ramesh'],
    "Age" : [10,20,30],
    "Place" : ['Mumbai','Delhi','Banglore']
}

df = pd.DataFrame(data)

print(df.info())