import pandas as pd
anish = {
    "Name":"Anish",
    "Age":19,
    "City":"Delhi"
}
piyush = {
    "Name":"Piyush",
    "Age":18,
    "City":"Agra"
}
manas = {
    "Name":"Manas",
    "Age":17,
    "City":"Mirzapur"
}
data = [anish,piyush,manas]
df = pd.DataFrame(data)
print(df)

df.to_csv("data.csv", index=False)