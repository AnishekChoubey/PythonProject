import pandas as pd
import matplotlib.pyplot as plt

marks = [45,77,95,58,63,75,32,84,73,28,94,27,53,84,73,57,94,37]

marks_series = pd.Series(marks)
plt.hist(marks_series,bins=5,color='magenta')

plt.title('Distribution of Marks Obtained by Students')
plt.xlabel("Marks Range")
plt.ylabel('Number of Students')

plt.show()

