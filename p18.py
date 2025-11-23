import matplotlib.pyplot as plt
years = [2018,2019,2020,2021]
sales = [289,299,311,357]

plt.plot(years,sales,marker='o',color='red',linestyle='-')

plt.title("Annual Sales Growth (2018-2021)")
plt.xlabel("Year")
plt.ylabel("Sales (in thousands)")
plt.show()
