import pandas as pd

dataframe = pd.read_csv("Week9/products.csv")

column = dataframe["Name"]

print(column)
print(dataframe)