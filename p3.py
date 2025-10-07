import pandas as pd

s1 = pd.Series(data=[21, 43, 73, 89, 67, 34, 96, 38, 13, 86])
s2 = pd.Series(data=[31, 77, 68, 23, 45, 93, 80, 79, 33, 66])

print("\nAddition:")
print(s1 + s2)
print("\nSubtraction:")
print(s1 - s2)
print("\nMultiplication:")
print(s1 * s2)
print("\nDivision:")
print(s1 / s2)

