import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Product':["Laptop","Tab","Smartphone","Monitor","Headphone"],
    'Sales':[465,395,673,120,489]
}

df = pd.DataFrame(data)
plt.bar(df['Product'],df['Sales'],color='cyan')

plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()
