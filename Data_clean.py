import pandas as pd

df = pd.read_csv("swiggy_orders_project.csv")
print(df)

df.columns = df.columns.str.strip()
print(df.columns.tolist())

Nancount = df.isnull().sum()
print(Nancount)

df.drop_duplicates()

df.to_csv("Clean_data.csv")
