import pandas as pd

df = pd.read_csv("vendas.csv", sep=",", encoding="utf-8")

print(df.head(2))

