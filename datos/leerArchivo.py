import pandas as pd

df = pd.read_csv("poblacion.csv")
# print(df)
# print(df.head())
# print(df.describe())
# print(df.tail())
# print(df.sample())

# print(df[["Date", "COL"]].to_string(index=False))

filtro = df[df['COL'] > 30000000]

# print(df[["Date", "COL"]])

print(filtro[['COL', 'ARG','ARE']])
