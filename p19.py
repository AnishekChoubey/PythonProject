import matplotlib.pyplot as plt

years = [2018,2019,2020,2021,2022]
sales_A = [150,180,220,210,260]
sales_B = [130,160,180,190,240]

plt.plot(years, sales_A, marker='o', color='blue', label='Product A')
plt.plot(years, sales_B, marker='o', color='red', label='Product B')

plt.xlabel("Annual Sales  Comparison (2018-2022)")
plt.xlabel("Year")
plt.ylabel("Sales (in thousands)")

plt.legend()

plt.savefig("sales_comparison.png")

plt.show()