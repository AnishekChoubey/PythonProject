import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year':[2015,2016,2017,2018,2019],
    'Revenue':[9824932,8372947,7923647,9374832,9373620]
}

df = pd.DataFrame(data)
plt.plot(df['Year'],df['Revenue'], marker='o',linestyle='-',color='r')

plt.title('Revenue per Year')
plt.xlabel('Year')
plt.ylabel('Revenue')

plt.show()