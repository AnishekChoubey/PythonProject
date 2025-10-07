import pandas as pd

s = pd.Series(["Anish","Manish","Manas","Piyush",
               "Vikram","Naitik","Ayush","Ishan",
               "Pratyush","Aman","Aryan"])

print("By Slicing:")
print(s[1:10:2])

print("\nBy Indexing:")
print(s[3])
print(s[9])

