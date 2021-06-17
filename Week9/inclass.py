import pandas as pd

dataframe = pd.read_csv("products.csv")

column = dataframe["Name"]

print(column)
print(dataframe)