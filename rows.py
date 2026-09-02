# head(n) -> shows first n rows if n is no written then shows first 5 rows by default
# tail(n) -> shows last n rows if n is no written then shows last 5 rows by default

import pandas as pd

df = pd.read_json("sample_Data.json")

# print(df.head(8))
# print(df.tail(8))

print(df.head())
print(df.tail())
